#!/bin/bash

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @newplaylist.json \
	http://127.0.0.1:5200/api/v1/collections/playlists/new

