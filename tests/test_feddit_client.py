import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

import requests

from src.feddit_client import get_comments

FEDDIT_API_URL = "http://localhost:8080/api/v1"


class TestGetComments(unittest.TestCase):
    @patch("requests.get")
    def test_get_comments_success(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {
            "comments": [
                {"id": 1, "text": "Great post!", "created_at": 1717357848},
                {"id": 2, "text": "Nice work.", "created_at": 1717354248},
            ]
        }
        mock_get.return_value = mock_response

        # Act
        comments = get_comments("1", 2)

        # Assert
        self.assertEqual(len(comments), 2)
        self.assertEqual(comments[0].id, "1")
        self.assertEqual(comments[0].text, "Great post!")
        self.assertEqual(comments[0].created_at, datetime.fromtimestamp(1717357848))
        self.assertEqual(comments[1].id, "2")
        self.assertEqual(comments[1].text, "Nice work.")
        self.assertEqual(comments[1].created_at, datetime.fromtimestamp(1717354248))

    @patch("requests.get")
    def test_get_comments_filter_by_start_date(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {
            "comments": [
                {"id": 1, "text": "Great post!", "created_at": 1717357848},
                {"id": 2, "text": "Nice work.", "created_at": 1717354248},
            ]
        }
        mock_get.return_value = mock_response
        start_date = datetime.fromtimestamp(1717355000)

        # Act
        comments = get_comments("1", 2, start_date=start_date)

        # Assert
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].id, "1")
        self.assertEqual(comments[0].text, "Great post!")
        self.assertEqual(comments[0].created_at, datetime.fromtimestamp(1717357848))

    @patch("requests.get")
    def test_get_comments_filter_by_end_date(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {
            "comments": [
                {"id": 1, "text": "Great post!", "created_at": 1717357848},
                {"id": 2, "text": "Nice work.", "created_at": 1717354248},
            ]
        }
        mock_get.return_value = mock_response
        end_date = datetime.fromtimestamp(1717355000)

        # Act
        comments = get_comments("1", 2, end_date=end_date)

        # Assert
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].id, "2")
        self.assertEqual(comments[0].text, "Nice work.")
        self.assertEqual(comments[0].created_at, datetime.fromtimestamp(1717354248))

    @patch("requests.get")
    def test_get_comments_raises_http_error(self, mock_get):
        # Arrange
        mock_get.side_effect = requests.exceptions.HTTPError

        # Act & Assert
        with self.assertRaises(requests.exceptions.HTTPError):
            get_comments("1", 2)

    @patch("requests.get")
    def test_get_comments_raises_connection_error(self, mock_get):
        # Arrange
        mock_get.side_effect = requests.exceptions.ConnectionError

        # Act & Assert
        with self.assertRaises(requests.exceptions.ConnectionError):
            get_comments("1", 2)


if __name__ == "__main__":
    unittest.main()
