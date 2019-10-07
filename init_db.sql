BEGIN TRANSACTION;
DROP TABLE IF EXISTS playlists;
CREATE TABLE playlists (
    id INTEGER primary key,
    title VARCHAR,
    user VARCHAR,
    desc VARCHAR,
    UNIQUE(id)
);

DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks (
	id INTEGER primary key,
	title VARCHAR,
	albumTitle VARCHAR,
	length INT,
	mediaURL VARCHAR,
	artURL VARCHAR,
	UNIQUE(id, albumTitle)
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	name VARCHAR,
	email VARCHAR,
	userid INTEGER primary key,
	bd VARCHAR,
	password VARCHAR,
	UNIQUE(email)
);

DROP TABLE IF EXISTS descriptions;
CREATE TABLE descriptions (
	descID INTEGER primary key,
	description VARCHAR,
	trackID INT,
	userID INT,
	UNIQUE(trackID, userID)
);
COMMIT;




