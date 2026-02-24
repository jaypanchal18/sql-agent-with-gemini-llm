import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import redis

class QueryExecutor:
    def __init__(self, db_url, redis_url):
        self.engine = create_engine(db_url)
        self.redis_client = redis.StrictRedis.from_url(redis_url)

    def execute_query(self, query, params=None):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(query), params)
                return [dict(row) for row in result]
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            return None

    def cache_query_result(self, query, result):
        try:
            self.redis_client.set(query, result)
        except redis.RedisError as e:
            print(f"Redis error occurred: {e}")

    def get_cached_result(self, query):
        try:
            return self.redis_client.get(query)
        except redis.RedisError as e:
            print(f"Redis error occurred: {e}")
            return None

    def execute_and_cache(self, query, params=None):
        cached_result = self.get_cached_result(query)
        if cached_result:
            return cached_result
        
        result = self.execute_query(query, params)
        if result is not None:
            self.cache_query_result(query, result)
        return result

# Example usage
# db_url = 'postgresql://user:password@localhost/dbname'
# redis_url = 'redis://localhost:6379/0'
# executor = QueryExecutor(db_url, redis_url)
# result = executor.execute_and_cache("SELECT * FROM users WHERE id = :id", {'id': 1})