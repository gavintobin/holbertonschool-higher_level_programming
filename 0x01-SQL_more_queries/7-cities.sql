-- creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL
	PRIMARY_KEY (id),
	UNIQUE(id),
	FOREIGN KEY (state_id) REFERENCE states(id));

