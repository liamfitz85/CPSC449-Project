#!/bin/bash

echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser.json \
	http://127.0.0.1:5000/api/v1/users/register

echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser2.json \
	http://127.0.0.1:5000/api/v1/users/register

echo "----------------------------------------------------------------------------------"


curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/1

echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/2

echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request DELETE \
	http://127.0.0.1:5000/api/v1/users/2

echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/register

echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request DELETE \
	http://127.0.0.1:5000/api/v1/users/2

echo "----------------------------------------------------------------------------------"