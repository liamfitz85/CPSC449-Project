import requests
import json

from xspf import xspf

x = xspf.Xspf()

r = requests.get("http://localhost:5200/api/v1/collections/playlists/all")
t = requests.get("http://localhost:5100/api/v1/collections/tracks/all")
playlist_list = r.json()
track_list = t.json()


file_urls = []

#print(playlist_list)
for i in playlist_list:
    #print(i['playListOfTracks'])
    tr = i['playListOfTracks'].strip('[]').split(',')
    for el in tr:
        #print(el)
        el = el.strip(' ').strip('\'')
        #print(el)
        file_urls.append(el)

        for f in file_urls:
            x.title = i['playTitle']
            #print(f)
            a = xspf.Track()
            for t in track_list:
                if f == t['trackMediaURL']:
                    print(i['playTitle'],i['playUserID'],i['playDesc'],t['trackID'], t['trackTitle'], t['trackAlbum'], t['trackArtist'], sep='\n')
                    #a.title = t['trackTitle']
                    #a.album = t['trackAlbum']
                    #x.add_track(a)

        file_urls=[]

#print(x.toXml())

# import xml.dom.minidom

# dom = xml.dom.minidom.parseString(x.toXml())

# print(dom.toprettyxml())