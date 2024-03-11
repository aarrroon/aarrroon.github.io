-- Drop the POI table if it exists
DROP TABLE IF EXISTS poi;

DROP TABLE IF EXISTS poi_type;


-- Create the POI table with a SERIAL primary key
CREATE TABLE poi (
    poi_id serial PRIMARY KEY,
    poi_name VARCHAR(30) NOT NULL,
    poi_price VARCHAR(5) NOT NULL,
    poi_lat DECIMAL(9, 6) NOT NULL,
    poi_long DECIMAL(9, 6) NOT NULL,
    poi_address VARCHAR(255) NOT NULL,
    poi_suburb VARCHAR(30) NOT NULL,
    poi_type_id int
);

CREATE TABLE poi_type (
    poi_type_id serial PRIMARY KEY,
    poi_type_name VARCHAR(30) NOT NULL
);

ALTER TABLE poi 
ADD CONSTRAINT poi_at_fk FOREIGN KEY (poi_type_id) 
REFERENCES poi_type(poi_type_id);

-- Insert activity types
INSERT INTO poi_type (
    poi_type_name
) VALUES (
    'Brunch Cafe'
),
(
    'Restaurant'
),
(
    'Activity'
);

-- Insert test rows into the POI table
INSERT INTO poi (
    poi_name,
    poi_price,
    poi_lat,
    poi_long,
    poi_address,
    poi_suburb,
	poi_type_id
) VALUES (
    'Wakuda',
    '$$',
    '-37.81244079607491',
    '144.96726826053194',
    'Centre, Mid City, Shop 201, 201/200 Bourke St, Melbourne VIC 3000',
    'Melbourne CBD',
    2
);