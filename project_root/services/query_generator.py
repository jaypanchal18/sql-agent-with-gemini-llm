import os
import json
import requests
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class QueryGenerator:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def generate_query(self, natural_language_query):
        try:
            response = self.call_gemini_api(natural_language_query)
            sql_query = self.extract_sql_from_response(response)
            return sql_query
        except Exception as e:
            current_app.logger.error(f"Error generating query: {str(e)}")
            return None

    def call_gemini_api(self, query):
        api_url = current_app.config['GEMINI_API_URL']
        headers = {
            'Authorization': f"Bearer {current_app.config['GEMINI_API_KEY']}",
            'Content-Type': 'application/json'
        }
        payload = {
            'query': query
        }
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Gemini API error: {response.status_code} - {response.text}")
        return response.json()

    def extract_sql_from_response(self, response):
        if 'sql' not in response:
            raise ValueError("SQL not found in response")
        return response['sql']

    def execute_query(self, sql_query):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(sql_query)
                return result.fetchall()
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error: {str(e)}")
            return None

def create_query_generator():
    db_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    return QueryGenerator(db_url)