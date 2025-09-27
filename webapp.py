from flask import Flask
from backend.routes.user_routes import user_bp
from backend.routes.general_routes import general_bp
from backend.data_logic.paths import ensure_dirs
from dotenv import load_dotenv
import os

ensure_dirs()
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))

app.register_blueprint(user_bp)
app.register_blueprint(general_bp)

if __name__ == "__main__":
    app.run(debug=True)