BEGIN TRANSACTION;
DROP TABLE IF EXISTS playlists;
CREATE TABLE playlists (
    	playID INTEGER primary key,
    	playTitle VARCHAR,
    	playUser VARCHAR,
    	playDesc VARCHAR,
	playListOfTracks VARCHAR, /*i have no idea how this works*/
   	UNIQUE(playID),
	FOREIGN KEY(playUser) REFERENCES users (userID)
);

DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks (
	trackID INTEGER primary key,
	trackTitle VARCHAR,
	trackAlbum VARCHAR,
	trackArtist VARCHAR,
	trackLength INT,
	trackMedia VARCHAR,
	trackArt VARCHAR,
	UNIQUE(trackID, trackMedia)
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
	FOREIGN KEY(trackID) REFERENCES tracks (trackID)
);

COMMIT;




