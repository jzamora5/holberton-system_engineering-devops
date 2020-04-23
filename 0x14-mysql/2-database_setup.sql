-- Database setup
-- In both servers
CREATE DATABASE IF NOT EXISTS tyrell_corp;

USE tyrell_corp;

CREATE TABLE IF NOT EXISTS nexus6 (
	id int PRIMARY KEY AUTO_INCREMENT,
	name varchar(255)
);

INSERT INTO nexus6 (name)

VALUES ("Leon");

GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
