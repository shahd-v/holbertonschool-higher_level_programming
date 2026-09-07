-- Lists shows that are not linked to any genre.
SELECT title FROM tv_shows WHERE id NOT IN (SELECT show_id FROM tv_show_genres) ORDER BY title ASC;
