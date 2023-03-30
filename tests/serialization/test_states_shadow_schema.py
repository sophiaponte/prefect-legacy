import prefectlegacy
from prefectlegacy.engine import state
from marshmallow import Schema


class StateSchema(Schema):
    pass


def test_state():
    """
    This test ensures that deserialization works even when
    another Marshmallow serializer called "StateSchema" has been
    created.

    https://github.com/PrefectHQ/prefect/pull/2738
    """
    a = state.Submitted(state=state.Success())
    prefectlegacy.serialization.state.StateSchema().load(a.serialize())
