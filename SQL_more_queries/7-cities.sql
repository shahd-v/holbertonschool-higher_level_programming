-- Creates the hbtn_0d_usa database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the hbtn_0d_usa database.
USE hbtn_0d_usa;
-- Creates cities with a foreign key to states.
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
