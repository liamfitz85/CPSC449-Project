-- :name user_by_id :one
SELECT userName, userUsername, userEmail FROM users
WHERE userID = :id;
