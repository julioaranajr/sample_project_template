import unittest
from unittest.mock import patch
from sample.get_zen import get_zen_success


class TestGetZen(unittest.TestCase):

    @patch("sample.get_zen.requests.get")
    def test_get_zen_success(self, mock_get):
        # Mock a successful response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = "Keep it logically awesome."
        mock_get.return_value = mock_response

        result = get_zen_success()
        self.assertEqual(result, "Keep it logically awesome.")
        mock_get.assert_called_once_with(
            "https://api.github.com/zen",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=5,
        )

    @patch("sample.get_zen.requests.get")
    def test_get_zen_failure(self, mock_get):
        # Mock a failed response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_zen_success()
        self.assertEqual(result, "Failed to get a Zen of GitHub.")
        mock_get.assert_called_once_with(
            "https://api.github.com/zen",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=5,
        )
