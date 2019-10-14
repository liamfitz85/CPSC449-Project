-- :name create_track :insert
INSERT INTO tracks(trackTitle, trackAlbum, trackArtist, trackLength, trackMediaURL, trackArt)
VALUES(:trackTitle, :trackAlbum, :trackArtist, :trackLength, :trackMediaURL, :trackArt)
