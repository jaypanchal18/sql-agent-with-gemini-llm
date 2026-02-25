import re
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

class QueryValidator:
    def __init__(self, db_session):
        self.db_session = db_session

    def validate_query(self, query):
        if not self.is_syntax_valid(query):
            raise ValueError("Invalid SQL syntax.")
        if self.is_injection_risk(query):
            raise ValueError("Potential SQL injection risk detected.")
        return True

    def is_syntax_valid(self, query):
        # Basic regex to check for common SQL syntax issues
        sql_syntax_pattern = re.compile(r'^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|TRUNCATE)\s+', re.IGNORECASE)
        return bool(sql_syntax_pattern.match(query))

    def is_injection_risk(self, query):
        # Check for common SQL injection patterns
        injection_patterns = [
            r'--',  # SQL comment
            r'\bOR\b',  # OR condition
            r'\bAND\b',  # AND condition
            r'\'',  # Single quote
            r'\"',  # Double quote
            r'\bEXEC\b',  # EXEC command
            r'\bUNION\b',  # UNION command
            r'\bSELECT\b',  # SELECT command
        ]
        for pattern in injection_patterns:
            if re.search(pattern, query, re.IGNORECASE):
                return True
        return False

    def execute_query(self, query):
        try:
            self.validate_query(query)
            result = self.db_session.execute(text(query))
            return result.fetchall()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database error occurred: {str(e)}")
        except ValueError as ve:
            raise RuntimeError(f"Validation error: {str(ve)}")