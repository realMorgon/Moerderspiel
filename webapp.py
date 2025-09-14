from flask import Flask
from backend.routes.user_routes import user_bp
from backend.routes.general_routes import general_bp
from backend.data_logic.paths import ensure_dirs

ensure_dirs()

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(general_bp)

if __name__ == "__main__":
    app.run(debug=True)