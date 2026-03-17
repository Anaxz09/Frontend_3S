import requests
from flask import request

base_url = 'https://api.thecatapi.com/v1'

def get_gatos():
    url = f"{base_url}/breeds"

    headers = {
        "x-api-key": "live_TwSawybgY5O80CDVRVkgZn5VZFlLgAXvXaRvo9FC0Hx4nMlnI04vUvPH2w7oWxpu"
    }




    resposta = requests.get(url, headers=headers)



    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)

    return resposta.json()[0]