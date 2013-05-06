import json, urllib

pages = raw_input('Number of pages: ')
page = 1
url = 'https://search.twitter.com/search.json?q=microsoft&page='
while page <= pages:
    response = urllib.urlopen(url + str(page))
    j = json.load(response)
    for item in j['results']:
        print item['text']
    page = page + 1
