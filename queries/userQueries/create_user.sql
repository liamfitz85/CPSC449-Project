-- :name create_user :insert
INSERT INTO users(userFirstName, userLastName, userMiddleName, userEmail, userBD, userPassword)
VALUES(:userFirstName, :userLastName, :userMiddleName, :userEmail, :userBD, :userPassword)