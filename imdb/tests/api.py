import unittest

import imdb

class TestActor(unittest.TestCase):

    def testInit(self):
        actor = imdb.actor('Christoph Waltz')

        try:
            imdb_id = actor.imdb_id
            short_desc = actor.short_desc
            name = actor.name
        except AttributeError as e:
            self.fail('Not returning correct actor model: %s' % e)

    def testGetActor(self):
        actor = imdb.actor('Christoph Waltz')

        self.assertEqual(actor.imdb_id, 'nm0910607')
        self.assertEqual(actor.name, 'Christoph Waltz')

    def testAutoCorrect(self):

        actor = imdb.actor('Tom Cruize')
        self.assertEqual(actor.name, 'Tom Cruise')


    def testLazyLoading(self):
        actor = imdb.actor('Christoph Waltz')

        try:
            films = actor.films
        except AttributeError as e:
            self.fail('Has no films attribute')

        self.assertNotEquals(films, None)

        try:
            photo = actor.photo
        except AttributeError:
            self.fail('Has no photo attribute')

        self.assertNotEquals(photo, None)

        try:
            description = actor.description
        except AttributeError:
            self.fail('Has no description attribute')

        self.assertNotEquals(description, None)

    def testNonExistent(self):
        actor = imdb.actor('a123asXZasdas')
        self.assertFalse(actor, 'Nonsense films should return False.')


class TestFilm(unittest.TestCase):

    def testInit(self):
        film = imdb.film('La Dolce Vita')

        try:
            imdb_id = film.imdb_id
            short_desc = film.short_desc
            name = film.name
        except AttributeError as e:
            self.fail('Not returning correct film model: %s' % e)

    def testGetActor(self):
        film = imdb.film('La Dolce Vita')

        self.assertEqual(film.imdb_id, 'tt0053779')
        self.assertEqual(film.name, 'La Dolce Vita')


    def testLazyLoading(self):
        film = imdb.film('La Dolce Vita')

        try:
            actors = film.actors
        except AttributeError as e:
            self.fail('Has no actors attribute')

        self.assertNotEquals(actors, None, 'Actors attribute not set correctly')
        self.assertNotEquals(actors, False, 'Actors attribute set to False')
        self.assertNotEquals(len(actors), 0, 'Actors attribute set to empty list')

        try:
            poster = film.poster
        except AttributeError:
            self.fail('Has no poster attribute')

        self.assertNotEquals(poster, None)
        self.assertNotEquals(poster, False)

        try:
            description = film.description
        except AttributeError:
            self.fail('Has no description attribute')

        self.assertNotEquals(description, None)
        self.assertNotEquals(description, False)


    def testAutoCorrect(self):

        film = imdb.film('La Dulce Vite')
        self.assertEqual(film.name, 'La Dolce Vita')

    def testNonExistent(self):
        film = imdb.film('a123asXZasdas')
        self.assertFalse(film, 'Nonsense films should return False.')

if __name__ == "__main__":
    unittest.main()

