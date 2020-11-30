import requests

url = 'https://jsonplaceholder.typicode.com/photos'
update_url = 'https://jsonplaceholder.typicode.com/photos/100'


def get_requests():
    response = requests.get(url)
    for item in response.json():
        print(item)


jsonPayload = {
    'albumId': 1,
    'title': 'test',
    'url': 'nothing_url.com',
    'thumbnailUrl': 'nothing_thumbnailUrl.com'
    }


def post_request():
    response = requests.post(url, json=jsonPayload)
    print(response.status_code)
    print(response.json())


def put_request():
    response = requests.put(update_url, json=jsonPayload)
    print(response.status_code, response.json())


def delete_request():
    response = requests.delete(update_url)
    print(response.status_code, response.json())


if __name__ == '__main__':
    get_requests()
    post_request()
    put_request()
    delete_request()

