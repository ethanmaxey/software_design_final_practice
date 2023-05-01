import requests

def validate_response(response):
    
    if 'unixtime' not in response:
        raise Exception("Invalid response from Worldtime API")

def get_response():
    return requests.get("http://worldtimeapi.org/api/ip").json()

def parse_response(response):
    
    validate_response(response)
    
    return response['unixtime']

def get_unixtime():
    return parse_response(get_response())