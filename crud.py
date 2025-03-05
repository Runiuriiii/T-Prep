from sqlalchemy.orm import Session
from models import User, Question, Answer, ReviewSchedule
from schemas import UserCreate, QuestionCreate, AnswerCreate, ReviewScheduleCreate
from utils import get_password_hash


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_question(db: Session, question: QuestionCreate, user_id: int):
    db_question = Question(**question.model_dump(), user_id=user_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def create_answer(db: Session, answer: AnswerCreate, question_id: int):
    db_answer = Answer(**answer.dict(), question_id=question_id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_questions_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Question).filter(Question.user_id == user_id).offset(skip).limit(limit).all()


def schedule_review(db: Session, review: ReviewScheduleCreate):
    db_review = ReviewSchedule(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_review_schedules(db: Session, question_id: int):
    return db.query(ReviewSchedule).filter(ReviewSchedule.question_id == question_id).all()
