-- List all records

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND TRIM(Name) <> ''
ORDER BY score DESC;
