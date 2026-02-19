import os
import requests
from flask import current_app
from sqlalchemy.exc import SQLAlchemyError

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.api_url = 'https://gemini.googleapis.com/v1/query'

    def generate_sql_query(self, natural_language_query):
        try:
            response = requests.post(
                self.api_url,
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                },
                json={'query': natural_language_query}
            )
            response.raise_for_status()
            return response.json().get('sql_query')
        except requests.exceptions.HTTPError as http_err:
            current_app.logger.error(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:
            current_app.logger.error(f'An error occurred: {err}')
            return None

    def execute_query(self, sql_query, db_session):
        try:
            result = db_session.execute(sql_query)
            db_session.commit()
            return result.fetchall()
        except SQLAlchemyError as e:
            db_session.rollback()
            current_app.logger.error(f'SQLAlchemy error occurred: {e}')
            return None

gemini_service = GeminiService()