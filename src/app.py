from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from handlers.routes import configure_routes

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Lexical Analysis"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

configure_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
