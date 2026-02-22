from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import redis
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['REDIS_URL'] = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

# Initialize extensions
db = SQLAlchemy(app)
redis_client = redis.from_url(app.config['REDIS_URL'])

# Example model
class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/example', methods=['GET', 'POST'])
def example_route():
    if request.method == 'POST':
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        new_entry = ExampleModel(data=data)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Entry created', 'id': new_entry.id}), 201

    entries = ExampleModel.query.all()
    return jsonify([{'id': entry.id, 'data': entry.data} for entry in entries]), 200

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the application: {e}")