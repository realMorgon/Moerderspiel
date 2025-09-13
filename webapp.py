from flask import Flask
from backend.routes.user_routes import bp
from backend.data_logic.paths import ensure_dirs

ensure_dirs()

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)