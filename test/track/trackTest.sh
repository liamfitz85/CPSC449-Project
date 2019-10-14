#!/bin/bash

echo "Testing post to insert without trackArt"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/track/testTrack.json \
	http://127.0.0.1:5100/api/v1/collections/tracks
echo 
echo 
echo 

echo "testing post to insert with all info in the json"
echo "----------------------------------------------------------"
curl --verbose \
        --request POST \
        --header 'Content-Type: application/json' \
        --data @test/track/testTrack2.json \
        http://127.0.0.1:5100/api/v1/collections/tracks
echo 
echo 
echo 


echo "testing post with missing fields"
echo "----------------------------------------------------------"
curl --verbose \
        --request POST \
        --header 'Content-Type: application/json' \
        --data @test/track/testTrack3.json \
        http://127.0.0.1:5100/api/v1/collections/tracks

echo 
echo 
echo 

echo "testing patch with all valid fields"
echo "----------------------------------------------------------"
curl --verbose \
        --request PATCH \
        --header 'Content-Type: application/json' \
        --data @test/track/editTrack.json \
        http://127.0.0.1:5100/api/v1/collections/tracks
echo 
echo 
echo 

echo "testing get all track"
echo "-------------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks/all
echo 
echo 
echo 

echo "testing get track_by_id"
echo "-------------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks/1
echo 
echo 
echo 

echo "testing get filter_by_id"
echo "-------------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks?trackID=1
echo 
echo 
echo 

echo "testing get filter_by_title"
echo "-------------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks?trackTitle=icarus
echo 
echo 
echo 

echo "testing get filter_by_album"
echo "-------------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks?trackAlbum=vertigo
echo 
echo 
echo 

echo "testing get filter_by_artist"
echo "-------------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks?trackArtist=EDEN

echo 
echo 
echo 

echo "testing get delete_by_id"
echo "-------------------------------------------------------------"
curl --verbose \
        --request DELETE \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5100/api/v1/collections/tracks/1