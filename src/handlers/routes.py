from flask import request
from lexical.compute_lexical_density import compute_ld


def configure_routes(app):
    @app.route('/')
    def hello():
        return 'Testing if this shows up! And it does. Yaaaay!'

    @app.route('/complexity', methods=['POST'])
    def lexical_analysis():
        try:
            request_data = request.get_json()
            input_text = request_data['input_text']
            mode = request.args.get('mode')
            computed_ld = compute_ld(input_text, mode)
            return computed_ld
        except KeyError as e:
            raise KeyError('Please enter valid input parameter', e)
    
