use db;

CREATE TABLE users(
  user_id INT NOT NULL,
  user_name VARCHAR(50) NOT NULL,
  creation_date VARCHAR(50) NOT NULL,
  PRIMARY KEY (user_id)
 );
  
INSERT INTO users(user_id, user_name, creation_date) VALUES 
(1,'dan1',NOW()),
(2,'dan2',NOW()),
(3,'dan3',NOW());