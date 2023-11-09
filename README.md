UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name = CONCAT(short_names.name, '.mp3') 
OR full_names.name = CONCAT(short_names.name, '.wav');


UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name = SUBSTRING(full_names.name, 0, POSITION('.' IN full_names.name) );


UPDATE full_names AS f
SET status = s.status
FROM short_names AS s
WHERE f.name = CONCAT(s.name, '.', SUBSTRING(f.name, POSITION('.' IN f.name) + 1));


