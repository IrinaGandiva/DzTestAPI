import pytest
import requests


class TestApiBreedsListAll:
    all_breeds_url = "https://dog.ceo/api/breeds/list/all"

    def test_status_code(self):
        response = requests.get(self.all_breeds_url)
        assert response.status_code == 200

    @pytest.mark.parametrize('main_breed, sub_breed', [
        ('affenpinscher', []),
        ('greyhound', ['italian']),
        ('setter', ['english', 'gordon', 'irish'])])
    def test_breeds_and_sub_breads(self, main_breed, sub_breed):
        r = requests.get(self.all_breeds_url)
        response = r.json()
        assert response['message'][main_breed] == sub_breed

    def test_status(self):
        r = requests.get(self.all_breeds_url)
        response = r.json()
        assert response["status"] == "success"

    @pytest.mark.parametrize('method_name', ['PUT', 'POST', 'DELETE'])
    def test_wrong_method(self, method_name):
        response = requests.request('method_name', self.all_breeds_url)
        assert response.status_code == 405

    @pytest.mark.parametrize('main_breed, sub_count', [
        ('affenpinscher', 0),
        ('greyhound', 1),
        ('setter', 3)])
    def test_count_of_sub_breeds(self, main_breed, sub_count):
        r = requests.get(self.all_breeds_url)
        response = r.json()
        assert len(response['message'][main_breed]) == sub_count
