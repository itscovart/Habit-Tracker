from sqlalchemy import Column, Integer, String, Boolean, Date
from app.db.session import Base
from datetime import date

class Habit(Base):
    __tablename__ = "Habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(Date, default=date.today)
    active = Column(Boolean, default=True)