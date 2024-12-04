import requests

BASE_URL = "http://localhost:5000/"

def get_user_info(username):
    films = requests.get(BASE_URL + username)
    return films