-- :name create_playlist :insert
INSERT INTO playlists(playTitle, playUser, playDesc, playListOfTracks)
VALUES(:playTitle, :playUser, :playDesc, :playListOfTracks)