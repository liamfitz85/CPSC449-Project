#!/bin/bash
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @newuser.json \
	http://127.0.0.1:5000/api/v1/user/register

