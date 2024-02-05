import json
import urllib.request
import urllib.parse
import urllib.error

import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    account = input('Enter Twitter Account:')
    if len(account) < 1:
        break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': account, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)  # urlopen() give us the content and bypass the header + store it for later
    data = connection.read().decode()
    headers = dict(connection.getheaders())  # we can get the header from .urlopen() with .getheaders()
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)  # ligne très commune
    print(json.dumps(js, indent=4))

    for user in js['users']:
        print(user['screen_name'])
        status = user['status']['text']
        print(' ', status[:50])
