-- :name create_playlist :insert
INSERT INTO playlists(playTitle, playUser, playDesc, playListOfTracks)
VALUES(:title, :user, :desc, :listOfTracks)
