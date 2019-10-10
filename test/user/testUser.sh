#!/bin/bash
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser.json \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser2.json \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser2.json \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/id/1
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/id/2
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/id/3
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request DELETE \
	http://127.0.0.1:5000/api/v1/users/id/2
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request DELETE \
	http://127.0.0.1:5000/api/v1/users/id/2
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/WassupMan404
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login2.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request PUT \
	--header 'Content-Type: application/json' \
	--data @test/user/updatepassword.json \
	http://127.0.0.1:5000/api/v1/users/WassupMan404/password
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login2.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo "----------------------------------------------------------------------------------"

curl --verbose \
	--request PUT \
	--header 'Content-Type: application/json' \
	--data @test/user/updatepassword2.json \
	http://127.0.0.1:5000/api/v1/users/WassupMan4daffaf04/password
echo
echo "----------------------------------------------------------------------------------"

