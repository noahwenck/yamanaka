import requests

BASE_URL = "http://localhost:5000/"

def get_user_info(username):
    films = requests.get(BASE_URL + "user/" + username)
    return films

def get_list_info(list_url):
    films = requests.get(BASE_URL + "list?list_url=" + list_url)
    return films