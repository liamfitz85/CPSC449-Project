#!/bin/bash

echo "POSITIVE CASE: insert description"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/description/newdescription.json \
	http://127.0.0.1:5300/api/v1/descriptions/
echo
echo "----------------------------------------------------------------------------------"

echo "POSITIVE CASE: insert description"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/description/newdescription2.json \
	http://127.0.0.1:5300/api/v1/descriptions/
echo
echo "----------------------------------------------------------------------------------"

echo "NEGATIVE CASE: insert description - missing post argument"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/description/newdescription3.json \
	http://127.0.0.1:5300/api/v1/descriptions/
echo
echo "----------------------------------------------------------------------------------"

echo "NEGATIVE CASE: insert description - invalid user"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/description/newdescription3.json \
	http://127.0.0.1:5300/api/v1/descriptions/
echo
echo "----------------------------------------------------------------------------------"

echo "POSITIVE CASE: get user all desription"
curl --verbose \
	--request GET \
	http://127.0.0.1:5300/api/v1/users/ad69/descriptions/all
echo
echo "----------------------------------------------------------------------------------"

echo "NEGATIVE CASE: get user all desription - invalid user"
curl --verbose \
	--request GET \
	http://127.0.0.1:5300/api/v1/users/invalid/descriptions/all
echo
echo "----------------------------------------------------------------------------------"

echo "POSITIVE CASE: get user all desription from track url"
curl --verbose \
	--request GET \
	http://127.0.0.1:5300/api/v1/users/ad69/descriptions?trackMediaURL=wwww%2Etrack%2EHURT
echo
echo "----------------------------------------------------------------------------------"

echo "NEGATIVE CASE: get user all desription - invalid url"
curl --verbose \
	--request GET \
	http://127.0.0.1:5300/api/v1/users/ad69/descriptions?trackMediaURL=wwww%invalid%2EHURT
echo
echo "----------------------------------------------------------------------------------"