default:
	./run_tests

test:
	coverage run --source=imdb run_tests
	coverage html
