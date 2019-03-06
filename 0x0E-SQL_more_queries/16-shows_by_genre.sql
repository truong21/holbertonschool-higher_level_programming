-- lists all shows and their genre
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.genre_id
RIGHT JOIN tv_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title;
