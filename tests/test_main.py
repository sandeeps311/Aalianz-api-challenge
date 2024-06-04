import unittest
from unittest.mock import patch
from src.models import Comment, CommentResponse
from src.sentiment_analysis import analyze_sentiment
from datetime import datetime

class TestAnalyzeSentiment(unittest.TestCase):

    @patch('src.sentiment_analysis.TextBlob')
    def test_analyze_sentiment_positive(self, mock_TextBlob):
        # Arrange
        mock_TextBlob_instance = mock_TextBlob.return_value
        mock_TextBlob_instance.sentiment.polarity = 0.5  # Mock positive sentiment
        comment = Comment(id='1', text='Great post!', created_at=datetime.now())

        # Act
        response = analyze_sentiment(comment)

        # Assert
        self.assertEqual(response.id, '1')
        self.assertEqual(response.text, 'Great post!')
        self.assertEqual(response.polarity, 0.5)
        self.assertEqual(response.classification, 'positive')

    @patch('src.sentiment_analysis.TextBlob')
    def test_analyze_sentiment_negative(self, mock_TextBlob):
        # Arrange
        mock_TextBlob_instance = mock_TextBlob.return_value
        mock_TextBlob_instance.sentiment.polarity = -0.5  # Mock negative sentiment
        comment = Comment(id='2', text='Poorly written post.', created_at=datetime.now())

        # Act
        response = analyze_sentiment(comment)

        # Assert
        self.assertEqual(response.id, '2')
        self.assertEqual(response.text, 'Poorly written post.')
        self.assertEqual(response.polarity, -0.5)
        self.assertEqual(response.classification, 'negative')

    @patch('src.sentiment_analysis.TextBlob')
    def test_analyze_sentiment_neutral(self, mock_TextBlob):
        # Arrange
        mock_TextBlob_instance = mock_TextBlob.return_value
        mock_TextBlob_instance.sentiment.polarity = 0.0  # Mock neutral sentiment
        comment = Comment(id='3', text='Okay post.', created_at=datetime.now())

        # Act
        response = analyze_sentiment(comment)

        # Assert
        self.assertEqual(response.id, '3')
        self.assertEqual(response.text, 'Okay post.')
        self.assertEqual(response.polarity, 0.0)
        self.assertEqual(response.classification, 'negative')

    @patch('src.sentiment_analysis.TextBlob')
    def test_analyze_sentiment_empty_comment(self, mock_TextBlob):
        # Arrange
        mock_TextBlob_instance = mock_TextBlob.return_value
        mock_TextBlob_instance.sentiment.polarity = 0.0  # Mock neutral sentiment
        comment = Comment(id='4', text='', created_at=datetime.now())

        # Act
        response = analyze_sentiment(comment)

        # Assert
        self.assertEqual(response.id, '4')
        self.assertEqual(response.text, '')
        self.assertEqual(response.polarity, 0.0)
        self.assertEqual(response.classification, 'negative')

if __name__ == '__main__':
    unittest.main()
