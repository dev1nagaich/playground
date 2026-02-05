from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database configuration
DB_CONNECTION_STRING = "sqlite:///./portfolio.db"

# Create database engine
db_engine = create_engine(
    DB_CONNECTION_STRING, connect_args={"check_same_thread": False}
)

# Session factory for database operations
DBSession = sessionmaker(bind=db_engine)

# Base class for all models
EntityBase = declarative_base()
