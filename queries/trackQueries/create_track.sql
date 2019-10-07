-- :name create_track :insert
INSERT INTO tracks(trackTitle, trackAlbum, trackArtist, trackLength, trackMedia, trackArt)
VALUES(:title, :albumTitle, :artist, :length, :mediaURL, :artURL)
