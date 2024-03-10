-- Drop the POI table if it exists
DROP TABLE IF EXISTS POI;

-- Create the POI table with a SERIAL primary key
CREATE TABLE POI (
    POI_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert test rows into the POI table
INSERT INTO POI (name) VALUES
('Test POI 1'),
('Test POI 2');

SELECT * FROM POI;
