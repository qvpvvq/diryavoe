from flask import Flask
import os
from dotenv import load_dotenv
from routes import simple_page
from database import close_connection, create_db
app = Flask(__name__)

load_dotenv()
DATABASE = os.getenv('DATABASE_URL', 'SQLi.db')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-if-not-set')
app.config['DATABASE_URL']=DATABASE 


app.teardown_appcontext(close_connection)

app.register_blueprint(simple_page)

if __name__ == "__main__":
    with app.app_context():
        create_db()
    app.run(debug=True, host='0.0.0.0') 