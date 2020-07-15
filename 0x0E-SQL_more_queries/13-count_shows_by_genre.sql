-- In db passed by argument hbtn_od_tvshows
-- List all genres and the number of times they are referenced
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_show_genres
INNER JOIN tv_genres on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
