import json, urllib

def print_tweets(pages):
    page = 1
    url = 'https://search.twitter.com/search.json?q=microsoft&page='
    while page <= pages:
        response = urllib.urlopen(url + str(page))
        j = json.load(response)
        for item in j['results']:
            print item['text']
            page = page + 1
