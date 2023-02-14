-- lists all shows containd in tv show db
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genre
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;
