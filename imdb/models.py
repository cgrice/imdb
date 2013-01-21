from .api import full_actor, full_film


class Actor(object):

    def __init__(self):
        self.name = None
        self.short_desc = None
        self.imbd_id = None

        # Set up properties to be None ready for lazy loading
        self.films = None
        self.photo = None
        self.description = None

    @property
    def films(self):
        if self.films is None:
            self._load_full(self)
        return self.films

    @property
    def photo(self):
        if self.photo is None:
            self._load_full(self)
        return self.photo

    @property
    def description(self):
        if self.description is None:
            self._load_full(self)
        return self.description

    def _load_full(self):
        (self.films, self.photo, self.description) = full_actor(self)
        return self


class Film(object):

    def __init__(self):
        self.name = None
        self.short_desc = None
        self.imbd_id = None

        # Set up properties to be None ready for lazy loading
        self.actors = None
        self.poster = None
        self.description = None

    @property
    def actors(self):
        return []

    @property
    def poster(self):
        return None

    @property
    def description(self):
        return None
