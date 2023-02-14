-- lists all shows without genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.title
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
