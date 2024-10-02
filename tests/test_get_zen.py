import unittest
from unittest.mock import patch
from sample.get_zen import get_zen_success


STATUS_OK = 200
STATUS_FAIL = 404


class TestGetZen(unittest.TestCase):
    """test get_zen_success function"""

    @patch("sample.get_zen.requests.get")
    def test_get_zen_success(self, mock_get: unittest.mock.Mock) -> None:
        """Test get_zen_success function"""
        mock_response = unittest.mock.Mock()
        mock_response.status_code = STATUS_OK
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
    def test_get_zen_failure(self, mock_get: unittest.mock.Mock) -> None:
        """Test get_zen_failure function"""
        mock_response = unittest.mock.Mock()
        mock_response.status_code = STATUS_FAIL
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
