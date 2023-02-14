-- list all cities in db
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.states_id = states.id
ORDER BY cities.id ASC;
