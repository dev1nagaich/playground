from sqlalchemy import Column, Integer, String, Text
from database import EntityBase

class UserProfile(EntityBase):
    __tablename__ = "user_profiles"

    profile_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email_address = Column(String)
    educational_background = Column(String)
    technical_skills = Column(Text)      # comma-separated values
    project_portfolio = Column(Text)     # newline-separated descriptions
    social_links = Column(Text)          # comma-separated URLs