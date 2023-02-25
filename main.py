import requests
import os

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

user_params = {
    'token': os.environ.get('PIXETOKEN'),
    'username': 'altrono',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(PIXELA_ENDPOINT, json=user_params)
print(response.text)

