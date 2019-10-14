#!/bin/bash

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/playlist/test.json \
	http://127.0.0.1:5200/api/v1/collections/playlists

echo 
echo 
echo 

echo "testing retieve playlist_by_id"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists/1

echo 
echo 
echo 

echo "testing delete_by_id"
echo "----------------------------------------------------------"
curl --verbose \
        --request DELETE \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists/3

echo 
echo 
echo 

echo "testing list all playlists"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists/all

echo 
echo 
echo 

echo "testing retieve playlist_by_user"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/users/ad69/playlists
echo 
echo 
echo 
echo "testing delete_by_id"
echo "----------------------------------------------------------"
curl --verbose \
        --request DELETE \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists/3

