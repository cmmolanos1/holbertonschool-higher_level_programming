-- Group the table as function of score

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
