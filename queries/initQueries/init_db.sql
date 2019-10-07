BEGIN TRANSACTION;
DROP TABLE IF EXISTS playlists;
CREATE TABLE playlists (
    	id INTEGER primary key,
    	title VARCHAR,
    	user VARCHAR,
    	desc VARCHAR,
   	UNIQUE(id),
	FOREIGN KEY(user) REFERENCES users (userID)
);

DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks (
	id INTEGER primary key,
	title VARCHAR,
	albumTitle VARCHAR,
	length INT,
	mediaURL VARCHAR,
	artURL VARCHAR,
	UNIQUE(id, mediaURL)
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	userID INTEGER PRIMARY KEY,
	userFirstName TEXT NOT NULL,
	userLastName TEXT NOT NULL,
	userMiddleName TEXT NOT NULL,
	userEmail TEXT NOT NULL,
	userBD TEXT NOT NULL,
	userPassword TEXT NOT NULL,
	UNIQUE(userEmail)
);

DROP TABLE IF EXISTS descriptions;
CREATE TABLE descriptions (
	descriptionID INTEGER PRIMARY KEY,
	descriptionDesc TEXT,
	trackID INT,
	userID INT,
	FOREIGN KEY(userID) REFERENCES users (userID),
	FOREIGN KEY(trackID) REFERENCES tracks (id)
);

COMMIT;




