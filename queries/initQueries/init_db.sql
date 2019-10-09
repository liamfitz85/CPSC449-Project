BEGIN TRANSACTION;
DROP TABLE IF EXISTS playlists;
CREATE TABLE playlists (
    	playID INTEGER primary key,
    	playTitle TEXT NOT NULL,
    	playUserID INT,
    	playDesc VARCHAR,
	playListOfTracks TEXT NOT NULL,
   	UNIQUE(playID),
	FOREIGN KEY(playUserID) REFERENCES users (userID) ON DELETE CASCADE
);

DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks (
	trackID INTEGER primary key,
	trackTitle VARCHAR NOT NULL,
	trackAlbum VARCHAR NOT NULL,
	trackArtist VARCHAR NOT NULL,
	trackLength INT NOT NULL,
	trackMedia VARCHAR NOT NULL,
	trackArt VARCHAR,
	UNIQUE(trackID, trackMedia)
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	userID INTEGER PRIMARY KEY,
	userName TEXT NOT NULL,
	userUserName TEXT NOT NULL,
	userEmail TEXT NOT NULL,
	userPassword TEXT NOT NULL,
	UNIQUE(userEmail)
);

DROP TABLE IF EXISTS descriptions;
CREATE TABLE descriptions (
	descriptionID INTEGER PRIMARY KEY,
	descriptionDesc TEXT,
	trackID INT,
	userID INT,
	FOREIGN KEY(userID) REFERENCES users (userID) ON DELETE CASCADE,
	FOREIGN KEY(trackID) REFERENCES tracks (trackID) ON DELETE CASCADE
);

COMMIT;




