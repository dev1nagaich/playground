from sqlalchemy import Column, Integer, String, Text
from db import Base

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    education = Column(String)
    skills = Column(Text)      # comma-separated
    projects = Column(Text)    # JSON-like string
    links = Column(Text)       # JSON-like string
