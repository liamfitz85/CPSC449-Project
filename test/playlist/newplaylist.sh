#!/bin/bash

echo"testing a regular post"
echo"-----------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/playlist/test.json \
	http://127.0.0.1:5200/api/v1/collections/playlists

echo 
echo 
echo 

echo "testing post without desc"
echo "----------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/playlist/test2.json \
	http://127.0.0.1:5200/api/v1/collections/playlists

echo 
echo 
echo 

echo "testing post failure with no content"
echo "----------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/playlist/test3.json \
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

echo "testing retieve playlist_by_id failure"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists/7

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

echo "testing retieve playlist_by_user failure"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/users/someDude/playlists
echo 
echo 
echo 

echo "testing delete_by_id failure by deleting nonexistant playlist"
echo "----------------------------------------------------------"
curl --verbose \
        --request DELETE \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists/3

echo 
echo 
echo 

echo "testing retieve playlist_by_id_filter"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists?playID=1

echo 
echo 
echo 

echo "testing retieve playlist_by_id_filter failure"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists?playID=7

echo 
echo 
echo 

echo "testing retieve playlist_by_title_filter"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists?playTitle=bruh

echo 
echo 
echo 

echo "testing retieve playlist_by_title_filter failure"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists?playTitle=someName

echo 
echo 
echo 

echo "testing retieve playlist_by_username_filter"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists?userName=ad69

echo 
echo 
echo 

echo "testing retieve playlist_by_username_filter"
echo "----------------------------------------------------------"
curl --verbose \
        --request GET \
        --header 'Content-Type: application/json' \
        http://127.0.0.1:5200/api/v1/collections/playlists?userName=someDude

