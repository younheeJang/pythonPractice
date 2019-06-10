import urllib.request
import json

#api represents: https://hacker-news.firebaseio.com/v0/item/11.json

base_url = 'https://hacker-news.firebaseio.com/v0/item/'


#decide and write how many items with hackernewsapi:
for itemid in range(1, 11):

    #make api's appearence:
    item_response = urllib.request.urlopen(base_url + str(itemid) + '.json')

    #could be using anythind read or readline except readall
    #response_string = item_response.readline().decode('utf-8')
    response_string = item_response.read().decode('utf-8')
    item = json.loads(response_string)

    #print results.
    print(item)

