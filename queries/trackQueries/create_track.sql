-- :name create_track :insert
INSERT INTO tracks(trackTitle, trackAlbum, trackArtist, trackLength, trackMedia, trackArt)
VALUES(:trackTitle, :trackAlbum, :trackArtist, :trackLength, :trackMedia, :trackArt)
