from .models import Actor, Film

import requests
import urllib

def actor(name, **kwargs):

    response = _person(name)

    actor = Actor()
    actor.imdb_id = response['id']
    actor.name = response['name']
    actor.short_desc = response['description']

    return actor


def film(name, **kwargs):

    response = _work(name)

    film = Film()
    film.imdb_id = response['id']
    film.name = response['title']
    film.short_desc = response['description']
    return film


def _person(name):
    response = _request("http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q=", name)

    if 'name_popular' in response:
        person = response['name_popular'][0]
    elif 'name_exact' in response:
        person = response['name_exact'][0]
    elif 'name_approx' in response:
        person = response['name_approx'][0]
    else:
        person = False

    return person


def _work(name):
    response = _request("http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=", name)

    if 'title_popular' in response:
        work = response['title_popular'][0]
    elif 'title_exact' in response:
        work = response['title_exact'][0]
    elif 'title_approx' in response:
        work = response['title_approx'][0]
    else:
        work = False

    return work


def _request(base_url, name):
    result = requests.get(base_url + urllib.quote_plus(name))
    return result.json()

