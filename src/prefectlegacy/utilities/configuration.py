"""
Utilities for interacting with [Prefect
configuration](https://docs.prefectlegacy.io/core/concepts/configuration.html).  These are only
intended to be used for testing.
"""
from contextlib import contextmanager
from typing import Iterator

import prefectlegacy
from prefectlegacy.configuration import Config


@contextmanager
def set_temporary_config(temp_config: dict) -> Iterator:
    """
    Temporarily sets configuration values for the duration of the context manager.

    This is only intended to be used for testing.

    Args:
        - temp_config (dict): a dictionary containing (possibly nested) configuration keys and
            values. Nested configuration keys should be supplied as `.`-delimited strings.

    Example:
        ```python
        with set_temporary_config({'setting': 1, 'nested.setting': 2}):
            assert prefectlegacy.config.setting == 1
            assert prefectlegacy.config.nested.setting == 2
        ```
    """
    try:
        old_config = prefectlegacy.config.copy()

        for key, value in temp_config.items():
            # the `key` might be a dot-delimited string, so we split on "." and set the value
            cfg = prefectlegacy.config
            subkeys = key.split(".")
            for subkey in subkeys[:-1]:
                cfg = cfg.setdefault(subkey, Config())
            cfg[subkeys[-1]] = value

        # ensure the new config is available in context
        with prefectlegacy.context(config=prefectlegacy.config):
            yield prefectlegacy.config
    finally:
        prefectlegacy.config.clear()
        prefectlegacy.config.update(old_config)
