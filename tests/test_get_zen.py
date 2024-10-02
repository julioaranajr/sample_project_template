"""Tests for the get_zen module."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from sample.get_zen import get_zen_api

STATUS_CODE_200 = 200
STATUS_CODE_404 = 404


class TestGetZenApi(unittest.TestCase):
    """Tests for the get_zen_api function."""

    @patch("sample.get_zen.requests.get")
    def test_get_zen_api(self, mock_get: unittest.mock.Mock) -> None:
        """Test the get_zen_api function."""
        mock_response = unittest.mock.Mock()
        mock_response.status_code = STATUS_CODE_200
        mock_response.text = "Keep it logically awesome."
        mock_get.return_value = mock_response

        result = get_zen_api()
        assert result == "Keep it logically awesome."
        mock_get.assert_called_once_with(
            "https://api.github.com/zen",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=5,
        )

    @patch("sample.get_zen.requests.get")
    def test_get_zen_failure(self, mock_get: unittest.mock.Mock) -> None:
        """Test the get_zen_api function when the request fails."""
        mock_response = unittest.mock.Mock()
        mock_response.status_code = STATUS_CODE_404
        mock_get.return_value = mock_response

        result = get_zen_api()
        assert result == "Failed to get a Zen of GitHub."
        mock_get.assert_called_once_with(
            "https://api.github.com/zen",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=5,
        )
