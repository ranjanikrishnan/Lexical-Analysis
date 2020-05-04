from flask import Flask, request
from lexical_density import get_lexical_density
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!..'


@app.route('/complexity', methods=['POST'])
def lexical_analysis():
    result = {}
    request_data = request.get_json()
    input_data = request_data['input_text']
    ld = get_lexical_density(input_data)
    result['data'] = {'overall_id': str(ld)}
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
