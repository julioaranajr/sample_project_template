"""Simple request to GitHub API.

This module makes a simple request to the GitHub API to get a random sentence

for the Zen of GitHub. More info: https://api.github.com/zen

Includes:
    requests: A simple HTTP library for Python to make requests.

Methods:
    get_zen: Get a random sentence from the Zen of GitHub.

Returns:
    str: A random sentence from the Zen of GitHub.
"""

from __future__ import annotations

import requests

STATUS_CODE = 200


def get_zen_api() -> str:
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
