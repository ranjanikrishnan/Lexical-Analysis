from flask import Flask, request
from lexical.compute_lexical_density import compute_ld

app = Flask(__name__)


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
