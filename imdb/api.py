from .models import Actor, Film
from .scraper import Scraper

scraper = Scraper()


def actor(name, **kwargs):

    actor = Actor()
    actor.name = 'Christoph Waltz'
    actor.picture = 'http://placekitten.com/200/300'
    return actor


def film(name, **kwargs):

    film = Film()
    return film


def full_film(film):
    return scraper.film(film.imbd_id)


def full_actor(actor):
    return scraper.actor(actor.imdb_id)


def _request(name, type):
    """
    http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q=christoph%20waltz
    http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=lost
    """
