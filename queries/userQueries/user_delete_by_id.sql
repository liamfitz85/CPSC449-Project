-- :name user_delete_by_id :one
DELETE FROM users
WHERE userID = :id;