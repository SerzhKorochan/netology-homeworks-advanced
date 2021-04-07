import requests

TOKEN = ''
HEADERS = {
    'Authorization': f'OAuth {TOKEN}'
}


def create_folder(folder_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
        'path': folder_name
    }

    response = requests.put(url, params=params, headers=HEADERS)

    return response.status_code


print(create_folder('NewFolder'))
