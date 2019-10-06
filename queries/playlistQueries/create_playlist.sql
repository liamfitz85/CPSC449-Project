-- :name create_playlist :insert
INSERT INTO playlists(title, user, desc, listOfTracks)
VALUES(:title, :user, :desc, :listOfTracks)
