import requests
import json

url = 'https://api.github.com/repos/wwvmd/kstreamspractice/issues/1'
token = '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'
custom_header = {'Authorization': 'token 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'}
response = requests.request(method='GET',url=url,headers=custom_header)
response_as_dict = json.loads(response.text)
print(response.text)
print(response_as_dict)
print(response_as_dict['body'])