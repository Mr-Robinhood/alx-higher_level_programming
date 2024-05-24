-- lists all shows in hbtn_0d_tvsows that have at least 1 genre linked
SELECT g.name AS genre, COUNT(tsg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.name
HAVING COUNT(tsg.tv_show_id) > 0
ORDER BY number_of_shows DESC;

