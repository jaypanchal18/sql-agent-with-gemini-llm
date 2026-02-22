import os
import requests
from flask import current_app
from sqlalchemy.exc import SQLAlchemyError

class GeminiIntegration:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.api_url = "https://gemini.googleapis.com/v1/query"

    def generate_sql_query(self, natural_language_query):
        try:
            response = requests.post(
                self.api_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"query": natural_language_query}
            )
            response.raise_for_status()
            sql_query = response.json().get('sql_query')
            if not sql_query:
                raise ValueError("No SQL query returned from Gemini.")
            return sql_query
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Request to Gemini API failed: {e}")
            raise RuntimeError("Failed to communicate with Gemini API.")
        except ValueError as e:
            current_app.logger.error(f"Error in response from Gemini API: {e}")
            raise RuntimeError("Invalid response from Gemini API.")
        except Exception as e:
            current_app.logger.error(f"An unexpected error occurred: {e}")
            raise RuntimeError("An unexpected error occurred while generating SQL query.")

    def execute_sql_query(self, sql_query, db_session):
        try:
            result = db_session.execute(sql_query)
            db_session.commit()
            return result.fetchall()
        except SQLAlchemyError as e:
            db_session.rollback()
            current_app.logger.error(f"SQL execution failed: {e}")
            raise RuntimeError("Failed to execute SQL query.")