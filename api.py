from .models import Actor, Film

def actor(name, **kwargs):

	actor = Actor()
	actor.name = 'Christoph Waltz'
	actor.picture = 'http://placekitten.com/200/300'
	return actor

def film(name, **kwargs):

	film = Film()
	return film

def _request(name, type):
	"""
	http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q=christoph%20waltz
	http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=lost
	"""