DROP TABLE IF EXISTS pizza;
DROP TABLE IF EXISTS pizza_products;
CREATE TABLE pizza (
	item_id INTEGER NOT NULL
	,name TEXT(100) NOT NULL
	,price NUMERIC(10, 2) NOT NULL
	,CONSTRAINT pizza_item_id PRIMARY KEY (item_id)
);

ALTER TABLE pizza
	RENAME TO pizza_products;

ALTER TABLE pizza_products
	ADD description TEXT(200);

INSERT INTO pizza_products VALUES (0,'Montanara',7.29,'Tomato sauce, mozzarella, mushrooms, pepperoni, and Stracchino (soft cheese)');
INSERT INTO pizza_products VALUES (1,'Margherita',4.59,'Tomato sauce, mozzarella, and oregano');
INSERT INTO pizza_products VALUES (2,'Marinara',8.99,'Tomato sauce, garlic and basil');
INSERT INTO pizza_products VALUES (3,'Quattro Stagioni',3.39,'Tomato sauce, mozzarella, mushrooms, ham, artichokes, olives, and oregano');
INSERT INTO pizza_products VALUES (4,'Carbonara',7.49,'Tomato sauce, mozzarella, parmesan, eggs, and bacon');
INSERT INTO pizza_products VALUES (5,'Frutti di Mare',6.79,'Tomato sauce and seafood');
INSERT INTO pizza_products VALUES (6,'Quattro Formaggi',7.99,'Tomato sauce, mozzarella, parmesan, gorgonzola cheese, artichokes, and oregano');
INSERT INTO pizza_products VALUES (7,'Crudo',8.79,'Tomato sauce, mozzarella and Parma ham');
INSERT INTO pizza_products VALUES (8,'Napoletana',6.49,'Tomato sauce, mozzarella, oregano, anchovies');
INSERT INTO pizza_products VALUES (9,'Pugliese',4.39,'Tomato sauce, mozzarella, oregano, and onions');

UPDATE pizza_products
SET price = 6.50
WHERE item_id = 3;

DELETE FROM pizza_products
WHERE name = 'Napoletana';