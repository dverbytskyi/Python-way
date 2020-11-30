import requests

url = 'https://api.github.com/user'


def get_user():
    response = requests.get(url, headers={'Authorization': 'Bearer {my_token}'})
    print(response.status_code, response.json())


if __name__ == '__main__':
    get_user()