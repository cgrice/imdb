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

    def testLazyLoading(self):
        actor = imdb.actor('Christoph Waltz')

        try:
            films = actor.films
        except AttributeError:
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

if __name__ == "__main__":
    unittest.main()

