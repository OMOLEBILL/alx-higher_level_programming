-- grouping counts
SELECT score, name
FROM second_table
GROUP BY score
HAVING score > 0
ORDER BY score DESC;
