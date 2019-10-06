-- :name create_track :insert
INSERT INTO tracks(title, albumTitle, artist, length, mediaURL, artURL)
VALUES(:title, :albumTitle, :artist, :length, :mediaURL, :artURL)
