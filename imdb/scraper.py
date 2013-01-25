import requests
from bs4 import BeautifulSoup


class Scraper(object):

	def actor(self, actor):
		page = self._get_page(self._build_url('name', actor))
		actor_image = self._extract_actor_image(page)
		films = self._extract_filmography(page)
		description = self._extract_actor_description(page)

		return {
			'films': films, 
			'image': actor_image, 
			'description': description
		}


	def film(self, film):
		page = self._get_page(self._build_url('title', film))

		return {
			'actors': False, 
			'image': False, 
			'description': False
		}

	def _get_page(self, url):
		response = requests.get(url)
		soup = BeautifulSoup(response.text, "html5lib")
		return soup


	def _build_url(self, type, imdb_id):
		url = "http://www.imdb.com/" + type + "/" + imdb_id + "/"
		return url


	def _extract_actor_image(self, page):
		img_td = page.find(id="img_primary")
		img_a = img_td.find('a')
		img = img_a.find('img')
		return img.get('src')

	def _extract_actor_description(self, page):
		return page.find(itemprop="description").text

	def _extract_filmography(self, page):
		films = []

		table = page.find(id="filmography")
		filmlist = table.find_all('div')[1]
		for row in filmlist.select('.filmo-row'):
			films.append(row.find_all('a')[0].text)

		return films

	def _extract_cast(self, page):
		return None