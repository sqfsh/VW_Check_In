import requests

url = 'https://oneapp-api.faw-vw.com/mycar/car-networking/charging/v1/get-charging-status-and-order?vin=LFVVB9E61P5029174&appkey=1678528261&signTimestamp=1732863417975&nonce=cb17d22e1b3a49828c8faf73478bb536&digitalSign=39994435bbdf388cd7ec1a32b7739c30'
headers = {
    'Authorization': 'tRf8y7XNgXZ_0UVj59cl2feYZy6Rys250AocK7vBi7HNlf53aIZeKXe8MsJIFqn5DOA7AL36YlTopqpN_9qKfMiOfS64EiNRZ6sT5dOdv9MK0muv7a8zJLAMicSHv4wpdIctbYBv3gpdFoYWLCym2YT4ZJtI_IzZRkncmI0BiYK65FtFwxuZNsdw'
}

response = requests.get(url, headers=headers)
print(response.text)
