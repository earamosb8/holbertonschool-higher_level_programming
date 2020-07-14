-- script that creates the table unique_id on your MySQL server
-- id has a default value of 1 and UNIQUE
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
