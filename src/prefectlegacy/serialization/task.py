from typing import TYPE_CHECKING, Any, Dict

from marshmallow import fields, post_load

import prefectlegacy
from prefectlegacy.utilities.serialization import (
    JSONCompatible,
    ObjectSchema,
    StatefulFunctionReference,
    to_qualified_name,
    SortedList,
)

if TYPE_CHECKING:
    import prefectlegacy.engine
    import prefectlegacy.engine.cache_validators
    import prefectlegacy.triggers


class TaskMethodsMixin:
    def get_attribute(self, obj: Any, key: str, default: Any) -> Any:
        """
        By default, Marshmallow attempts to index an object, then get its attributes.
        Indexing a Task results in a new IndexTask, so for tasks we use getattr(). Otherwise
        we use the default method.
        """
        if isinstance(obj, prefectlegacy.Task):
            return getattr(obj, key, default)
        else:
            return super().get_attribute(obj, key, default)  # type: ignore

    def load_inputs(self, task: prefectlegacy.core.Task) -> Dict[str, Dict]:
        if not isinstance(task, prefectlegacy.core.Task):
            return self.get_attribute(task, "inputs", None)
        inputs = {}
        for k, v in task.inputs().items():
            inputs[k] = dict(required=v["required"], type=str(v["type"]))
        return inputs

    def load_outputs(self, task: prefectlegacy.core.Task) -> str:
        if not isinstance(task, prefectlegacy.core.Task):
            return self.get_attribute(task, "outputs", None)
        return str(task.outputs())

    @post_load
    def create_object(self, data: dict, **kwargs: Any) -> prefectlegacy.core.Task:
        """
        Sometimes we deserialize tasks and edges simultaneously (for example, when a
        Flow is being deserialized), in which case we check slugs to see if we already
        deserialized a matching task. In that case, we reload the task from a shared
        cache.
        """
        slug = data.get("slug")
        auto_generated = data.pop("auto_generated", False)

        # if the slug is not in the task cache, create a task object and add it
        if slug not in self.context.setdefault("task_cache", {}):  # type: ignore
            task = super().create_object(data)  # type: ignore
            task.auto_generated = auto_generated  # type: ignore
            self.context["task_cache"][slug] = task  # type: ignore

        # return the task object from the cache
        return self.context["task_cache"][slug]  # type: ignore


class TaskSchema(TaskMethodsMixin, ObjectSchema):
    class Meta:
        object_class = lambda: prefectlegacy.core.Task
        exclude_fields = ["type", "inputs", "outputs"]

    type = fields.Function(lambda task: to_qualified_name(type(task)), lambda x: x)
    name = fields.String(allow_none=True)
    slug = fields.String(allow_none=True)
    tags = SortedList(fields.String())
    max_retries = fields.Integer(allow_none=True)
    retry_delay = fields.TimeDelta(allow_none=True)
    inputs = fields.Method("load_inputs", allow_none=True)
    outputs = fields.Method("load_outputs", allow_none=True)
    timeout = fields.Integer(allow_none=True)
    trigger = StatefulFunctionReference(
        valid_functions=[
            prefectlegacy.triggers.all_finished,
            prefectlegacy.triggers.manual_only,
            prefectlegacy.triggers.always_run,
            prefectlegacy.triggers.all_successful,
            prefectlegacy.triggers.all_failed,
            prefectlegacy.triggers.any_successful,
            prefectlegacy.triggers.any_failed,
            prefectlegacy.triggers.some_failed,
            prefectlegacy.triggers.some_successful,
        ],
        # don't reject custom functions, just leave them as strings
        reject_invalid=False,
        allow_none=True,
    )
    skip_on_upstream_skip = fields.Boolean(allow_none=True)
    cache_for = fields.TimeDelta(allow_none=True)
    cache_key = fields.String(allow_none=True)
    cache_validator = StatefulFunctionReference(
        valid_functions=[
            prefectlegacy.engine.cache_validators.never_use,
            prefectlegacy.engine.cache_validators.duration_only,
            prefectlegacy.engine.cache_validators.all_inputs,
            prefectlegacy.engine.cache_validators.all_parameters,
            prefectlegacy.engine.cache_validators.partial_inputs_only,
            prefectlegacy.engine.cache_validators.partial_parameters_only,
        ],
        # don't reject custom functions, just leave them as strings
        reject_invalid=False,
        allow_none=True,
    )
    auto_generated = fields.Boolean(allow_none=True)


class ParameterSchema(TaskMethodsMixin, ObjectSchema):
    class Meta:
        object_class = lambda: prefectlegacy.core.parameter.Parameter  # type: ignore
        exclude_fields = ["type", "outputs", "slug"]

    type = fields.Function(lambda task: to_qualified_name(type(task)), lambda x: x)
    name = fields.String(required=True)
    slug = fields.String(allow_none=True)
    default = JSONCompatible(allow_none=True)
    required = fields.Boolean(allow_none=True)
    tags = SortedList(fields.String())
    outputs = fields.Method("load_outputs", allow_none=True)
