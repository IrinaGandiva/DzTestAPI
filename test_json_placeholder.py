import pytest
import requests


class TestApiJsonPlaceholder:
    def test_comments_post_id(self):
        _url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
        r = requests.get(_url)
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['postId'] == 1

    def test_comments_id(self):
        _url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
        r = requests.get(_url)
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['id'] == i + 1

    def test_creation_new_post(self):
        _url = 'https://jsonplaceholder.typicode.com/posts'
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        new_title = 'this is a new title'
        body = {'title': new_title}
        r = requests.post(_url, headers=headers, json=body, verify=False)
        assert r.status_code == 201
        response = r.json()
        assert response['title'] == new_title

    @pytest.mark.parametrize('number, post_id', [(1, 1), (2, 2)])
    def test_posts_post_id(self, number, post_id):
        _url = f'https://jsonplaceholder.typicode.com/posts/{number}/comments'
        r = requests.get(_url)
        assert r.status_code == 200
        response = r.json()
        for i in range(len(response)):
            assert response[i]['postId'] == post_id

    @pytest.mark.parametrize('number, email', [(1, 'Eliseo@gardner.biz'), (2, 'Presley.Mueller@myrl.com')])
    def test_posts_email(self, number, email):
        _url = f'https://jsonplaceholder.typicode.com/posts/{number}/comments'
        r = requests.get(_url)
        assert r.status_code == 200
        response = r.json()
        count = 0
        for i in range(len(response)):
            if response[i]['email'] == email:
                count += 1
            assert count == 1
