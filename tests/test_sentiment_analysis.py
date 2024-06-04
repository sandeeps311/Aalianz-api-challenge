import unittest
from unittest.mock import patch
from src.models import Comment
from src.sentiment_analysis import analyze_sentiment


from datetime import datetime


class TestAnalyzeSentiment(unittest.TestCase):
    @patch("src.sentiment_analysis.TextBlob")
    def test_analyze_sentiment_positive(self, mock_TextBlob):
        # Arrange
        mock_TextBlob_instance = mock_TextBlob.return_value
        mock_TextBlob_instance.sentiment.polarity = 0.5  # Mock positive sentiment
        comment = Comment(
            id="1", text="Great post!", created_at=datetime.now()
        )  # Provide a default value for created_at

        # Act
        response = analyze_sentiment(comment)

        # Assert
        self.assertEqual(response.id, "1")
        self.assertEqual(response.text, "Great post!")
        self.assertEqual(response.polarity, 0.5)
        self.assertEqual(response.classification, "positive")

    @patch("src.sentiment_analysis.TextBlob")
    def test_analyze_sentiment_negative(self, mock_TextBlob):
        # Arrange
        mock_TextBlob_instance = mock_TextBlob.return_value
        mock_TextBlob_instance.sentiment.polarity = -0.5  # Mock negative sentiment
        comment = Comment(
            id="2", text="Poorly written post.", created_at=datetime.now()
        )  # Provide a default value for created_at

        # Act
        response = analyze_sentiment(comment)

        # Assert
        self.assertEqual(response.id, "2")
        self.assertEqual(response.text, "Poorly written post.")
        self.assertEqual(response.polarity, -0.5)
        self.assertEqual(response.classification, "negative")


if __name__ == "__main__":
    unittest.main()
