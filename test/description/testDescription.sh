#!/bin/bash
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/description/newdescription.json \
	http://127.0.0.1:5300/api/v1/descriptions/
echo
echo "----------------------------------------------------------------------------------"