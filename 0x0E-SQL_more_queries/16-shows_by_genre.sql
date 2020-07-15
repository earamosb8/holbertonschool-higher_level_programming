-- script that lists all shows, and all genres linked to that show, from the database
-- If a show doesn't have a genre, display NULL in the genre column
SELECT title, name
FROM tv_show_genres
RIGHT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY title, name ASC;
