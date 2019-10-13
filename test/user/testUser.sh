#!/bin/bash
echo "POSITIVE CASE: insert user"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser.json \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo
echo


echo "POSITIVE CASE: insert user"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser2.json \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo
echo


echo "NEGATIVE CASE: insert user - duplicate user"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/newuser2.json \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo
echo


echo "TESTING CASE: show all user"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo
echo


echo "POSITIVE CASE: GET user by id"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/id/1
echo
echo
echo


echo "POSITIVE CASE: GET user by id"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/id/2
echo
echo
echo


echo "NEGATIVE CASE: GET user by id - invalid id"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/id/100
echo
echo
echo

echo "POSITIVE CASE: DELETE user by id "
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request DELETE \
	http://127.0.0.1:5000/api/v1/users/id/2
echo
echo
echo

echo "TESTING CASE: show all user"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/register
echo
echo
echo
echo "----------------------------------------------------------------------------------"

echo "NEGATIVE CASE: DELETE user by id -  id no longer valid "
curl --verbose \
	--header 'Content-Type: application/json' \
	--request DELETE \
	http://127.0.0.1:5000/api/v1/users/id/2
echo
echo
echo

echo "POSITIVE CASE: GET user by username"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--header 'Content-Type: application/json' \
	--request GET \
	http://127.0.0.1:5000/api/v1/users/WassupMan404
echo
echo
echo

echo "POSITIVE CASE: Login"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo
echo

echo "NEGATIVE CASE: Login - wrong password"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login2.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo
echo
echo "----------------------------------------------------------------------------------"

echo "POSITIVE CASE: Update password"
curl --verbose \
	--request PUT \
	--header 'Content-Type: application/json' \
	--data @test/user/updatepassword.json \
	http://127.0.0.1:5000/api/v1/users/WassupMan404/password
echo
echo
echo

echo "POSITIVE CASE: Login"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login2.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo
echo

echo "NEGATIVE CASE: Login - wrong password"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request POST \
	--header 'Content-Type: application/json' \
	--data @test/user/login.json \
	http://127.0.0.1:5000/api/v1/users/login
echo
echo
echo

echo "NEGATIVE CASE: Update password - user doesn't exist"
echo "----------------------------------------------------------------------------------"
curl --verbose \
	--request PUT \
	--header 'Content-Type: application/json' \
	--data @test/user/updatepassword2.json \
	http://127.0.0.1:5000/api/v1/users/WassupMan4daffaf04/password
echo
echo
echo
echo "----------------------------------------------------------------------------------"

