from flask import Flask
import os
from dotenv import load_dotenv
from routes import simple_page
from database import close_connection, create_db

from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
    resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5174",  # Для npm run dev
                "http://localhost",  # Для Docker (порт 80)
                "http://127.0.0.1",  # На всякий случай
            ]
        }
    },
)

load_dotenv()
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key-if-not-set")
app.config["DATABASE_URL"] = os.getenv("DATABASE_URL", "SQLi.db")


app.teardown_appcontext(close_connection)
app.register_blueprint(simple_page, url_prefix="/api")

if __name__ == "__main__":
    with app.app_context():
        create_db()

    app.run(debug=True, host="0.0.0.0")
