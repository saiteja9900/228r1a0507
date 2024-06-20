from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Correct Base declaration
Base = declarative_base()

# Define the Students class
class Students(Base):
    __tablename__ = 'students'  # Table name
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key column
    name = Column(String(50), nullable=False)
    Rollno = Column(String(20), unique=True, nullable=False)
    Section = Column(String(10), nullable=False)

# Example of setting up the engine and session (assuming SQLite for demonstration)
# engine = create_engine('sqlite:///students.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
