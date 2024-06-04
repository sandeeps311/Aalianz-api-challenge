import requests
from typing import List, Optional
from src.models import Comment
from datetime import datetime

FEDDIT_API_URL = "http://localhost:8080/api/v1"


def get_comments(
    subfeddit: str,
    limit,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> List[Comment]:
    url = f"{FEDDIT_API_URL}/comments/?subfeddit_id={subfeddit}&limit={limit}"

    response = requests.get(url)
    response.raise_for_status()
    comments_data = response.json()
    print(comments_data)
    comments_data = comments_data.get("comments", [])
    print(comments_data)
    comments = [
        Comment(
            id=str(comment["id"]),
            text=comment["text"],
            created_at=datetime.fromtimestamp(comment["created_at"]),
        )
        for comment in comments_data
    ]

    if start_date:
        comments = [comment for comment in comments if comment.created_at >= start_date]
    if end_date:
        comments = [comment for comment in comments if comment.created_at <= end_date]

    return comments
