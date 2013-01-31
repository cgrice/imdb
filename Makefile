default:
	./test_imdb.py

test:
	coverage run --source=imdb test_imdb.py
	coverage html
