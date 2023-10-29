import requests

def lambda_handler(event, context) -> str:
    word_count = event['wordCount']
    url = f'https://random-word-api.herokuapp.com/word?number={int(word_count)}'
    response = requests.get(url)
    return ', '.join(response.json()).upper()

