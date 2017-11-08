import requests
import simplejson

r = requests.get('https://github.com/timeline.json')
c = r.content
j = simplejson.loads(c)
for item in r.json():
    print(j)

    print(item['documentation_url'][0])