-- Create user for the replica server
-- On primary MySQL server only (web-01)
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
