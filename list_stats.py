import asyncio
import io
import json
from gather import get_user_info, get_list_info

LIST_URLS = [
    "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/",
    "https://letterboxd.com/dave/list/imdb-top-250/",
    "https://letterboxd.com/oscars/list/oscar-winning-films-best-picture/",
    "https://letterboxd.com/brsan/list/cannes-palme-dor-winners/",
    "https://letterboxd.com/matthew/list/all-time-worldwide-box-office/",
    "https://letterboxd.com/afi/list/afis-100-years100-movies-10th-anniversary/",
    "https://letterboxd.com/bfi/list/sight-and-sounds-greatest-films-of-all-time/",
    "https://letterboxd.com/gubarenko/list/1001-movies-you-must-see-before-you-die-2024/",
    "https://letterboxd.com/crew/list/edgar-wrights-1000-favorite-movies/",
    "https://letterboxd.com/dvideostor/list/roger-eberts-great-movies/",
    "https://letterboxd.com/jack/list/women-directors-the-official-top-250-narrative/",
    "https://letterboxd.com/jack/list/black-directors-the-official-top-100-narrative/",
    "https://letterboxd.com/jack/list/official-top-250-films-with-the-most-fans/",
    "https://letterboxd.com/jack/list/official-top-250-documentary-films/",
    "https://letterboxd.com/lifeasfiction/list/letterboxd-100-animation/",
    "https://letterboxd.com/darrencb/list/letterboxds-top-250-horror-films/"
]

async def compute_watched_from_official_lists(username, user_films):
    """
    Computes the number of films watched by a user from all official Letterboxd lists. Prints outputs.

    :param username: Letterboxd Username
    """
    user_films_json = json.loads(user_films)

    tasks = [compute_watched_from_provided_list(username, user_films_json, url) for url in LIST_URLS]
    await asyncio.gather(*tasks)

async def compute_watched_from_provided_list(username, user_films, url):
    """
    Computes the number of films watched by a user from the provided list. Prints outputs.

    :param username: Letterboxd Username
    :param user_films: JSON of user films
    :param url: url of list to compare against
    """
    list_response = get_list_info(url).text
    list_as_list = list_response.split(',')
    list_name = list_as_list.pop(0)
    list_name = list_name[2:len(list_name)-1]

    """ 
    Parsing the list name - ORDER IS IMPORTANT
    1. Re-add spaces that were removed in web scraper
    2. Replace ONLY the character of \\u2019 (Caused by Edgar Wright's list)
    3. Replace all \\u (other apostrophes)
    4. Replace any Quotes that are escaped (Roger Ebert's list)
    Add outliers as needed
    """
    list_name = list_name.replace('-', " ")\
        .replace("\\u2019", "'")\
        .replace("\\u", "")\
        .replace("\\\"", "\"")

    # Since the first element is the list name, if we don't properly remove it - the json creation will fail
    try:
        list = json.loads("[" + ','.join(list_as_list))
    except json.JSONDecodeError as e:
        print(f"Error parsing list: {list_name}")
        print(f"JSONDecodeError: {e}")
        # print(f"FOR DEBUGGING: {list_as_list}") # Dump whatever the list is

    # Remove the ranking from the list if it exists - cleaner comparison
    if 'Ranking' in list[0]:
        for film in list:
            del film['Ranking']

    matches = 0
    for film in list:
        if film in user_films:
            matches+= 1

    percentage = round(matches / len(list) * 100)

    print(f"{username} has watched {matches} / {len(list)} ({percentage}%) films from the {list_name} list.")
