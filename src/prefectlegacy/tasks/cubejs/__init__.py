"""
This is a collection of tasks to interact with a Cube.js or Cube Cloud environment.
"""

try:
    from prefectlegacy.tasks.cubejs.cubejs_tasks import CubeJSQueryTask
except ImportError as err:
    raise ImportError(
        'prefectlegacy.tasks.cubejs` requires Prefect to be installed with the "cubejs" extra.'
    ) from err
