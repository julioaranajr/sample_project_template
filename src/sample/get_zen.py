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

import requests


def get_zen_success():
    """Get a random sentence from the Zen of GitHub."""
    url = "https://api.github.com/zen"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        return response.text
    return "Failed to get a Zen of GitHub."


# Uncomment the following lines to test the function
# if __name__ == "__main__":
#     print(get_zen_success())
