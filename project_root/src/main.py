from flask import Flask
from src.views import main_routes

app = Flask(__name__)

app.register_blueprint(main_routes)

if __name__ == "__main__":
    app.run(debug=True)
