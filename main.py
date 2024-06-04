from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from src.models import Comment, CommentResponse
from src.feddit_client import get_comments
from src.sentiment_analysis import analyze_sentiment
# from app.dependencies import get_query_params

app = FastAPI()


@app.get("/comments", response_model=List[CommentResponse])
def read_comments(subfeddit: str,
                  limit:int,
                  start_date: Optional[datetime] = Query(None),
                  end_date: Optional[datetime] = Query(None),
                  sort_by_polarity: bool = False):
    comments = get_comments(subfeddit,limit, start_date, end_date)
    analyzed_comments = [analyze_sentiment(comment) for comment in comments]

    if sort_by_polarity:
        analyzed_comments.sort(key=lambda x: x.polarity, reverse=True)

    return analyzed_comments
