import warnings
warnings.filterwarnings('ignore')

import requests
import json

# Cisco Prime Credentials
user = 'elkrestapi'
pwd = 'E1k@R3s+!'

first_r = 0
last_r = 0
max_r = 1000

dict_list = list()

def get_all_aps(first_r, max_r):
    # Setting up url
    url = 'https://prime.ltfinc.net/webacs/api/v3/data/AccessPoints.json?.full=t                                                                                        rue&.firstResult={0}&.maxResults={1}'.format(first_r, max_r)
    # Setting up headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), verify=False)
    return response.json()['queryResponse']

while True:
    response = get_all_aps(first_r, max_r)
    for entity in response['entity']:
        dict_list.append(json.loads(json.dumps(entity['accessPointsDTO']).replac                                                                                        e('@', '')))
    last = response['@last']
    count = response['@count']

    if last + 1 >= count:
        break
    else:
        first_r = last + 1

print(json.dumps(dict_list))
