import pytest
import requests


class TestApiBreweries:
    base_url = 'https://api.openbrewerydb.org/breweries'

    def test_search_by_name(self):
        search_query = 'Jacket'
        _url = f"{self.base_url}/search?query={search_query}"
        r = requests.get(_url)
        assert r.status_code == 200
        response = r.json()
        assert search_query in response[0]['name']

    @pytest.mark.parametrize('type_name', ['closed', 'planning'])
    def test_filter_by_type(self, type_name):
        r = requests.get(self.base_url, params={'by_type': type_name})
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['brewery_type'] == type_name

    @pytest.mark.parametrize('per_page, count', [(1, 1), (0, 0), (21, 21)])
    def test_count_of_items(self, per_page, count):
        r = requests.get(self.base_url, params={'page': '1', 'per_page': per_page})
        assert r.status_code == 200
        response = r.json()
        assert len(response) == count

    @pytest.mark.parametrize('brew_id', [1, 2, 123])
    def test_get_by_valid_id(self, brew_id):
        _url = self.base_url + f"/{brew_id}"
        r = requests.get(_url)
        assert r.status_code == 200
        response = r.json()
        assert response['id'] == brew_id

    @pytest.mark.parametrize('brew_id', [-1, 0, 'text'])
    def test_get_by_not_valid_id(self, brew_id):
        _url = self.base_url + f"/{brew_id}"
        r = requests.get(_url)
        assert r.status_code == 404
        response = r.json()
        assert response['message'] == f"Couldn't find Brewery with 'id'={brew_id}"
