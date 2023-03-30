"""
This module contains a collection of tasks for interacting with AWS resources.

All AWS related tasks can be authenticated using the `AWS_CREDENTIALS` Prefect Secret that should be a dictionary with two keys: `"ACCESS_KEY"` and `"SECRET_ACCESS_KEY"`.  See [Third Party Authentication](../../../orchestration/recipes/third_party_auth.html) for more information.
"""
try:
    from prefectlegacy.tasks.aws.s3 import S3Download, S3Upload, S3List
    from prefectlegacy.tasks.aws.lambda_function import (
        LambdaCreate,
        LambdaDelete,
        LambdaInvoke,
        LambdaList,
    )
    from prefectlegacy.tasks.aws.step_function import StepActivate
    from prefectlegacy.tasks.aws.secrets_manager import AWSSecretsManager
    from prefectlegacy.tasks.aws.parameter_store_manager import AWSParametersManager
    from prefectlegacy.tasks.aws.batch import BatchSubmit
    from prefectlegacy.tasks.aws.client_waiter import AWSClientWait
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.aws` requires Prefect to be installed with the "aws" extra.'
    ) from err

__all__ = [
    "AWSClientWait",
    "AWSSecretsManager",
    "AWSParametersManager",
    "BatchSubmit",
    "LambdaCreate",
    "LambdaDelete",
    "LambdaInvoke",
    "LambdaList",
    "S3Download",
    "S3List",
    "S3Upload",
    "StepActivate",
]
