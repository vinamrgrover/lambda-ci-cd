import requests

def lambda_handler(event = None, context = None) -> str:
    url = 'https://random-word-api.herokuapp.com/word?length=5'
    response = requests.get(url)
    return ''.join(response.json()).upper()

