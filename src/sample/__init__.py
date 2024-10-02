from __future__ import annotations

from .run import main
from .version import version as __version__

__all__ = (
    "__version__",
    "main",
)

import platform

import requests

STATUS_CODE = 200


if platform.python_implementation() == "PyPy":

    def get_zen_success() -> str:
        """Get a random sentence from the Zen of GitHub."""
        url = "https://api.github.com/zen"
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == STATUS_CODE:
            return response.text
        return "Failed to get a Zen of GitHub."

else:

    def get_zen_success() -> str:
        """Get a random sentence from the Zen of GitHub."""
        url = "https://api.github.com/zen"
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == STATUS_CODE:
            return response.text
        return "Failed to get a Zen of GitHub."
