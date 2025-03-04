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

def create_card(db: Session, card: CardCreate, subject_id: int):
    db_card = Card(**card.model_dump(), subject_id=subject_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def get_cards_by_subject(db: Session, subject_id: int, skip: int = 0, limit: int = 100):
    return db.query(Card).filter(Card.subject_id == subject_id).offset(skip).limit(limit).all()

def create_correct_answer(db: Session, answer: CorrectAnswerCreate, card_id: int):
    db_answer = CorrectAnswer(**answer.model_dump(), card_id=card_id)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def create_definition(db: Session, definition: DefinitionCreate, card_id: int):
    db_definition = Definition(**definition.model_dump(), card_id=card_id)
    db.add(db_definition)
    db.commit()
    db.refresh(db_definition)
    return db_definition

def schedule_review(db: Session, review: ReviewScheduleCreate):
    db_review = ReviewSchedule(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_review_schedules(db: Session, question_id: int):
    return db.query(ReviewSchedule).filter(ReviewSchedule.question_id == question_id).all()
