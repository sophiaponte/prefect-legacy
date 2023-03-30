import os
import subprocess

import prefectlegacy


def test_prefect_version_is_updated_everywhere():
    """
    Tests that prefectlegacy.__version__ matches the version defined in setup.py
    """
    current_version = prefectlegacy.__version__

    cwd = os.path.dirname(os.path.dirname(__file__))
    cmd = ["python", "setup.py", "--version"]
    setup_version = subprocess.check_output(cmd, cwd=cwd).strip().decode()

    assert setup_version == current_version
