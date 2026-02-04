from sqlalchemy import Column, Integer, Float, Date
from app.db.session import Base
from datetime import date

class Run(Base):
    __tablename__ = "runs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=date.today)
    distance_km = Column(Float, nullable=False)
    duration_min = Column(Float, nullable=False)
