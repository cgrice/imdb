from .scraper import Scraper

scraper = Scraper()

class Actor(object):

    def __init__(self):
        self.name = None
        self.short_desc = None
        self.imdb_id = None

        # Set up properties to be None ready for lazy loading
        self._films = None
        self._photo = None
        self._description = None


    def __repr__(self):
        return ('<%s: %s - %s>' % (self.imdb_id, self.name, self.short_desc))

    @property
    def films(self):
        if self._films is None:
            self._load_full()
        return self._films

    @films.setter
    def films(self, films):
        self._films = films

    @property
    def photo(self):
        if self._photo is None:
            self._load_full()
        return self._photo

    @photo.setter
    def photo(self, photo):
        self._photo = photo

    @property
    def description(self):
        if self._description is None:
            self._load_full()
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def _load_full(self):
        fullinfo = full_actor(self)

        self.films = fullinfo['films']
        self.description = fullinfo['description']
        self.photo = fullinfo['image']

        return self


class Film(object):

    def __init__(self):
        self.name = None
        self.short_desc = None
        self.imbd_id = None

        # Set up properties to be None ready for lazy loading
        self._actors = None
        self._poster = None
        self._description = None

    def __repr__(self):
        return ('<%s: %s - %s>' % (self.imdb_id, self.name, self.short_desc))

    @property
    def actors(self):
        if self._actors is None:
            self._load_full()
        return self._actors

    @actors.setter
    def actors(self, actors):
        self._actors = actors

    @property
    def poster(self):
        if self._poster is None:
            self._load_full()
        return self._poster

    @poster.setter
    def poster(self, poster):
        self._poster = poster

    @property
    def description(self):
        if self._description is None:
            self._load_full()
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def _load_full(self):
        fullinfo = full_film(self)

        self.actors = fullinfo['actors']
        self.description = fullinfo['description']
        self.poster = fullinfo['image']

        return self


def full_film(film):
    return scraper.film(film.imdb_id)


def full_actor(actor):
    return scraper.actor(actor.imdb_id)

