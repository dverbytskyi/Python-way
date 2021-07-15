import requests

url = 'https://api.github.com/user'


def get_user():
    response = requests.get(url, headers={'Authorization': 'Bearer {token}'})
    # print(response.status_code, response.json())
    my_json = response.json()
    for key, value in my_json.items():
        print(key, value)
    print(my_json['id'])


if __name__ == '__main__':
    get_user()