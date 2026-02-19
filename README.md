# SQL Agent with Gemini LLM  ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Project Description
SQL Agent with Gemini LLM is an intelligent SQL agent that leverages Google Gemini LLM to convert natural language queries into SQL statements, execute them against various databases, and return the results in a user-friendly format. This project includes features such as query validation, connection pooling, and support for multiple database backends, making it a versatile tool for developers and data analysts.

## Features
- 🗣️ Natural language processing to generate SQL queries using Google Gemini LLM
- ⚙️ Execution of generated SQL queries against multiple database backends (PostgreSQL, MySQL, SQLite)
- 📊 Formatted results returned in JSON or HTML format
- ✅ Query validation to ensure SQL syntax correctness before execution
- 🔗 Connection pooling for efficient database connections
- 🔒 User authentication and role-based access control
- 🌐 Interactive web interface for users to input natural language queries
- 📜 Logging and monitoring of executed queries for auditing purposes

## Tech Stack
### Frontend
- 🌐 **Flask** (Web Framework)

### Backend
- 🐍 **Python** (Programming Language)
- 🧠 **Google Gemini LLM** (Natural Language Processing)

### Database
- 🗄️ **PostgreSQL** (Database)
- 🗄️ **MySQL** (Database)
- 🗄️ **SQLite** (Database)
- 🗄️ **SQLAlchemy** (ORM)

### Caching
- 🧊 **Redis** (In-memory Data Structure Store)

## Installation
To set up the project locally, follow these steps:

- Clone the repository
bash
git clone https://github.com/jaypanchal18/sql-agent-with-gemini-llm.git
- Navigate into the project directory
bash
cd sql-agent-with-gemini-llm
- Create a virtual environment
bash
python -m venv venv
- Activate the virtual environment
bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
- Install the required packages
bash
pip install -r requirements.txt
- Set up the database (PostgreSQL, MySQL, or SQLite) as per your preference.

## Usage
To start the application, run the following command:
bash
flask run
Access the web interface at `http://127.0.0.1:5000` and input your natural language queries.

## API Documentation
For API usage, refer to the [API Documentation](https://github.com/jaypanchal18/sql-agent-with-gemini-llm/wiki/API-Documentation).

## Testing
To run the tests, execute the following command:
bash
pytest
## Deployment
For deploying the application, follow these steps:

- Ensure your production environment has the necessary dependencies installed.
- Configure your web server (e.g., Gunicorn, Nginx) to serve the Flask application.
- Set environment variables for database connections and other configurations.

## Contributing
We welcome contributions! Please follow these steps:

- Fork the repository
- Create a new branch (`git checkout -b feature/YourFeature`)
- Make your changes and commit them (`git commit -m 'Add some feature'`)
- Push to the branch (`git push origin feature/YourFeature`)
- Open a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for their support.
- Special thanks to Google for providing the Gemini LLM technology.