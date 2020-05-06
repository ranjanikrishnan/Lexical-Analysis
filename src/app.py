from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from lexical.compute_lexical_density import compute_ld

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


@app.route('/')
def hello():
    return 'Testing if this shows up! And it does. Yaaaay!'


@app.route('/complexity', methods=['POST'])
def lexical_analysis():
    try:
        request_data = request.get_json()
        input_text = request_data['input_text']
        mode = request.args.get('mode')
        computed_ld = compute_ld(mode, input_text)
        return computed_ld
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
