import requests
from pprint import pprint

import mayan


MAYAN_TOKEN = 'Token ?????????????XXXXXXXXXXXX'
MAYAN_API = 'http://127.0.0.1:8000/api/'
session = requests.Session()
headers = {'Authorization': MAYAN_TOKEN}

# pprint(requests.get('http://127.0.0.1:8000/api/document_types/', headers=headers).json())


session.headers.update(headers)

page = session.get(MAYAN_API + 'document_types/').json()

DOCUMENT_TYPES = MAYAN_API + 'document_types/'

DOCUMENT_NO = '1/'

DOCUMENT_URL = DOCUMENT_TYPES + DOCUMENT_NO + 'documents/'

document = session.get(DOCUMENT_URL).json()

count = document['count']
results = document['results'] # list of json
documents_urls = [result['latest_version']['download_url'] for result in results]
documents_labels = [result['label'] for result in results]

# print(documents_urls)
# print(documents_labels)
# pprint(document)

downloaded = session.get(documents_urls[2]).text
# pprint(downloaded)

# upload a new document

with open('/home/ying/Desktop/Papers/LanguageModels/attention.pdf', mode='rb') as file_object:
    response = session.post('http://127.0.0.1:8000/api/documents/', files={'file': file_object}, data={'document_type': 1})
    resp_json = response.json()
    print(response)




