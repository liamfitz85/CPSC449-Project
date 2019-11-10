import requests
import json

from xspf import xspf

x = xspf.Xspf()

r = requests.get("http://localhost:5200/api/v1/collections/playlists/all")

json_list = json.loads(r.text)
play_list = []

for l in json_list:
    x.title = l['playTitle']
    play_list.append(x)
    for i in list(l['playListOfTracks']):
        print(i)
    x = xspf.Xspf()

for l in play_list:
    print(l.toXml())
