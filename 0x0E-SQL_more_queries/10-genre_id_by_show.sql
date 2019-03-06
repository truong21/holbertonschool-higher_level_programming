-- database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id
ORDER by tv_shows.title, tv_show_genres.genre_id;
