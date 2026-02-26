from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')

class Database:
    def __init__(self):
        self.engine = self.create_engine()
        self.Session = sessionmaker(bind=self.engine)

    def create_engine(self):
        try:
            engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_timeout=30, pool_recycle=1800)
            return engine
        except SQLAlchemyError as e:
            print(f"Error creating engine: {e}")
            raise

    def get_session(self):
        try:
            session = self.Session()
            return session
        except SQLAlchemyError as e:
            print(f"Error getting session: {e}")
            raise

    def close_session(self, session):
        try:
            session.close()
        except SQLAlchemyError as e:
            print(f"Error closing session: {e}")
            raise

db = Database()