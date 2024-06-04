from textblob import TextBlob
from src.models import Comment, CommentResponse

def analyze_sentiment(comment: Comment) -> CommentResponse:
    blob = TextBlob(comment.text)
    polarity = blob.sentiment.polarity
    classification = "positive" if polarity > 0 else "negative"
    return CommentResponse(id=comment.id, text=comment.text, polarity=polarity, classification=classification)
