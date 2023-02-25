import requests
import os
os.environ['PIXETOKEN'] = 'awsedddwdsdsfdgfhgjhjhjh'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
# TOKEN = os.environ.get('PIXETOKEN')
USERNAME = 'altronos'
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# # print(response.text)
grapth_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

grapth_config = {
    'id': 'graph1',
    'name': 'Memory focus',
    'unit':"Km",
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': 'awsedddwdsdsfdgfhgjhjhjh'
}


response = requests.post(url=grapth_endpoint, json=grapth_config, headers=headers)

print(response.text)
