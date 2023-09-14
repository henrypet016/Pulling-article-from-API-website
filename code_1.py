import requests
import json
response_API = requests.get('https://api.elifesciences.org/articles/84711')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['title']
date = parse_json['published']
print("This is the title of the article: ", info)
print("And it was published on: ", date) 