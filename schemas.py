from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Во всех моделях ответов заменить Config.orm_mode
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Было orm_mode = True
        # Дополнительные настройки если необходимо


class QuestionBase(BaseModel):
    question_text: str


class QuestionCreate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True


class AnswerBase(BaseModel):
    answer_text: str


class AnswerCreate(AnswerBase):
    pass


class AnswerResponse(AnswerBase):
    id: int
    question_id: int
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class ReviewScheduleBase(BaseModel):
    next_review: datetime
    stage: int


class ReviewScheduleCreate(ReviewScheduleBase):
    question_id: int


class ReviewScheduleResponse(ReviewScheduleBase):
    id: int
    class Config:
        from_attributes = True
