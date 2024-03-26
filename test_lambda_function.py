# test_lambda_function.py

import json
from lambda_function import lambda_handler

def test_successful_update():
    event = {
        'body': {
            'id': '123',
            'Weather': 'Sunny'
        }
    }
    response = lambda_handler(event, {})
    assert response['statusCode'] == 200

def test_missing_attributes():
    event = {
        'body': {
            'Weather': 'Sunny'
        }
    }
    response = lambda_handler(event, {})
    assert response['statusCode'] == 400

def test_additional_attributes():
    event = {
        'body': {
            'id': '123',
            'Weather': 'Sunny',
            'Extra': 'Attribute'
        }
    }
    response = lambda_handler(event, {})
    assert response['statusCode'] == 400
