from flask import Flask
from backend.routes.user_routes import user_bp
from backend.routes.general_routes import general_bp
from backend.routes.session_routes import session_bp
from backend.data_logic.paths import ensure_dirs
from dotenv import load_dotenv
import os
from flask_session import Session

ensure_dirs()
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", os.urandom(24))
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './data/flask_session/'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 604800  # 7d
Session(app)

app.register_blueprint(user_bp)
app.register_blueprint(general_bp)
app.register_blueprint(session_bp)

if __name__ == "__main__":
    app.run(debug=True)