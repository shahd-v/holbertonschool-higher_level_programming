-- Creates the hbtn_0d_usa database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the hbtn_0d_usa database.
USE hbtn_0d_usa;
-- Creates the states table with an auto-incrementing primary key.
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
