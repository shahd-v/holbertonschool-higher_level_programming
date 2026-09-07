-- Lists states and their cities, including states without cities.
SELECT states.name, cities.id, cities.name FROM states LEFT JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC;
