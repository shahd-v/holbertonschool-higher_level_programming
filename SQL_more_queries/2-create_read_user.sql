-- Creates the hbtn_0d_2 database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user_0d_2 if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants user_0d_2 read-only access to hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
