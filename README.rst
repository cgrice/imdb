=============
imdb
=============

About
=====

imdb.py is a small, clean api to get data out of IMDb. It's designed to be as simple as possible to use, only fetching additional data when requested.

Installing
-----

python setup.py install


Running
=======

.. code-block:: pycon

    >>> import imdb
    >>> imdb.actor('Christoph Waltz')
    <nm0910607: Christoph Waltz - Actor, Inglourious Basterds>
    >>> actor = imdb.actor('Christoph Waltz')
    >>> actor
    <nm0910607: Christoph Waltz - Actor, Inglourious Basterds>
    >>> actor.films[0:5]
    [u'Reykjavik', u'The Zero Theorem', u'Epic', u'Django Unchained', u'Carnage']
    >>> actor.photo
    u'http://ia.media-imdb.com/images/M/MV5BMTI4MzMxMTMxM15BMl5BanBnXkFtZTcwNzE3NjQxMw@@._V1._SY314_CR3,0,214,314_.jpg'
    >>> imdb.film('Goodfellas')
    <tt0099685: Goodfellas - 1990, Martin Scorsese>
    >>> film = imdb.film('Goodfellas')
    >>> film.poster
    u'http://ia.media-imdb.com/images/M/MV5BMjU3MTQ4OTA0MV5BMl5BanBnXkFtZTYwNjAyMDg4._V1_SY317_CR7,0,214,317_.jpg'
    >>> film.actors[0:5]
    [u' Robert De Niro\n', u' Ray Liotta\n', u' Joe Pesci\n', u' Lorraine Bracco\n', u' Paul Sorvino\n']
