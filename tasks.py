from datetime import datetime, timedelta

from celery import Celery
from models import ReviewSchedule
from database import SessionLocal

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task
def schedule_notification(question_id: int, interval: int):
    db = SessionLocal()
    next_review = datetime.now() + timedelta(seconds=interval)
    review_schedule = ReviewSchedule(
        question_id=question_id,
        next_review=next_review,
        stage=interval
    )
    db.add(review_schedule)
    db.commit()
    db.close()