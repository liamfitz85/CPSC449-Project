-- :name playlist_by_username :one
SELECT P.playID, P.playTitle, P.playAlbum, P.desc, P.ListOfTracks, U.userName FROM playlist as P, users as U WHERE U.userName = :username AND P.playUserID = U.userID;
