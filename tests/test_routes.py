from flask import Flask
import json
from handlers.routes import configure_routes


def test_base_route(create_app):
    client = create_app
    url = '/'
    response = client.get(url)
    assert response.get_data() == b'Testing if this shows up! And it does. Yaaaay!'
    assert response.status_code == 200


def test_complexity_route(create_app):
    client = create_app
    url = '/complexity'

    mock_request_data = {"input_text": "Kim loves going to the cinema. And he loves to eat popcorn there. That's what I think."}
    response = client.post(url, data=json.dumps(mock_request_data), content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['data'] == {"overall_ld": "0.71"}
