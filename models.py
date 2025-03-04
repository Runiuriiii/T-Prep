from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True) 
    cards = relationship("Card", backref="subject", cascade="all, delete-orphan") 

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum("question", "rule", name="card_type"), nullable=False)  
    card_text = Column(String, nullable=False)  
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False) 
    correct_answer = relationship("CorrectAnswer", uselist=False, back_populates="card")  
    definition = relationship("Definition", uselist=False, back_populates="card") 

class CorrectAnswer(Base):
    __tablename__ = "correct_answers"
    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id", ondelete="CASCADE"), unique=True)
    answer_text = Column(String, nullable=False)  
    card = relationship("Card", back_populates="correct_answer")

class Definition(Base):
    __tablename__ = "definitions"
    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id", ondelete="CASCADE"), unique=True)
    definition_text = Column(String, nullable=False) 
    card = relationship("Card", back_populates="definition")

class ReviewSchedule(Base):
    __tablename__ = "review_schedules"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    next_review = Column(DateTime)
    stage = Column(Integer)
