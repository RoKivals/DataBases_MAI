DROP TABLE IF EXISTS specification;
DROP TABLE IF EXISTS sales_markets;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS models_range;
DROP TABLE IF EXISTS models_sales_markets_relation;
DROP TABLE IF EXISTS body_type;
DROP TYPE IF EXISTS engine_type;

CREATE TYPE engine_type AS ENUM (
	'hybrid',
	'electric',
	'internal combustion engine'
);

CREATE TABLE body_type (
	id bigserial primary key,
	name varchar(255) NOT NULL
);

CREATE TABLE models_range (
	id bigserial primary key,
	company_id bigint NOT NULL,
	model_name varchar(55) NOT NULL
)

CREATE TABLE companies(
    id bigserial primary key,
    name varchar(255) NOT NULL,
    office varchar(255) NOT NULL,
    creation_date date NOT NULL,
    count_of_workers int
);

CREATE TABLE specification (
    id bigserial primary key,
    model_id bigint NOT NULL,
    start_of_production date,
    end_of_production date,
    engine engine_type,
    engine_displacement int,
    HP int,
    body_type bigint NOT NULL,
	FOREIGN KEY (body_type) REFERENCES body_type
	ON DELETE SET NULL
	ON UPDATE CASCADE,
	FOREIGN KEY (model_id) REFERENCES models_range
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE sales_markets (
    id bigserial primary key,
    market_zone varchar(255) NOT NULL
);

CREATE TABLE models_sales_markets_relation (
	id bigserial primary key,
	model_id bigint NOT NULL, 
	sales_market_id bigint NOT NULL,
	FOREIGN KEY (model_id) REFERENCES models_range
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	FOREIGN KEY (sales_market_id) REFERENCES sales_markets
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE model_body_type_relation (
	model_id bigint NOT NULL, 
	body_type_id bigint NOT NULL,
	FOREIGN KEY (model_id) REFERENCES models_range
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	FOREIGN KEY (body_type_id) REFERENCES body_type
	ON DELETE CASCADE
	ON UPDATE CASCADE
)

CREATE TRIGGER model_body_type_relation_insert
AFTER INSERT ON specification
FOR EACH ROW
BEGIN
    INSERT INTO model_body_type_relation (model_id, body_type_id) VALUES (NEW.model_id, NEW.body_type);
END;

CREATE UNIQUE INDEX IF NOT EXISTS uix_companies_name ON companies (name);
CREATE UNIQUE INDEX IF NOT EXISTS uix_body_type_name ON body_type (name);
CREATE UNIQUE INDEX IF NOT EXISTS uix_sales_market_market_zone ON sales_markets (market_zone);
CREATE UNIQUE INDEX IF NOT EXISTS uix_models_sales_markets_relation ON models_sales_markets_relation (model_id, sales_market_id);

INSERT
INTO sales_markets (market_zone) VALUES 
('Europe'),
('Russia'),
('Asia'),
('China'),
('USA'),
('South America'),
('Africa'),
('India');

INSERT
INTO body_type (name) VALUES 
('Hatchback'),
('Coupe'),
('Sedan'),
('Station wagon'),
('Kammback'),
('Cabriolet'),
('Roadster'),
('Targa'),
('CrossOver'),
('Jeep'),
('Pickup'),
('Limousine'),
('Minivan'),
('Campervan');

INSERT
INTO companies (name, office, creation_date, count_of_workers) VALUES
('Acura'),
('Alfa Romeo'),
('Aston Martin'),
('Audi', 'Ingolstadt', '16.07.1909', 87000),
('Bentley'),
('BMW', 'Munich', '07.03.1916', 118909),
('Bugatti'),
('BYD'),
('Cadillac'),
('Chevrolet'),
('Crysler'),
('Citroen'),
('Dacia'),
('Dodge'),
('Ferrari'),
('Fiat'),
('Ford', 'Las Vegas', '16.06.1903', 183000),
('Haval'),
('Honda'),
('Hummer'),
('Infiniti'),
('Jeep'),
('KIA'),
('Lada'),
('Lamborghini'),
('Lexus'),
('Lotus'),
('Maserati', 'Modena', '01.12.1914', 1100),
('Mazda', 'Hiroshima', '30.01.1920', 49786),
('Mercedes-Benz', 'Stuttgart', '28.06.1926', 145436),
('Mini'),
('Pagani'),
('Porsche', 'Stuttgart', '06.03.1931', 36359),
('Rolls-Royce'),
('Skoda'),
('Subaru'),
('Tesla'),
('Toyota'),
('Volkswagen', 'Wolfsburg', '28.05.1937', 670000);

INSERT INTO models_range(company_id, name)
SELECT (id, UNNEST (ARRAY['Golf', 'ID.4']) from companies where name = 'Volkswagen' LIMIT 1);

(1, 'Golf'),
(1, 'ID.4'),
(1, 'Golf'),
(1, 'Golf'),
(1, 'Golf'),
(1, 'Golf'),
(1, 'Golf'),
(1, 'Golf'),
(1, 'Golf'),


INSERT
INTO models (company_id, name, release_date, body_type) VALUES 
(1, 'Golf', '01.01.1974', 1),
(1, 'ID.4', '01.01.2020', 9),
(2, 'A1', '01.01.2010', 1),
(2, 'A2', '01.01.1999', 1),
(2, 'A4', '01.01.1994', 3),
(2, 'A5', '01.06.2007', 2),
(2, 'A6', '01.01.1994', 3),
(2, 'A7', '01.01.2010', 5),
(2, 'A8', '01.01.1994', 3),
(3, 'Cayenne', '01.12.2002', 9),
(3, '911', '01.01.1965', 8),
(4, 'Focus', '01.01.1998', 1),
(4, 'F-150', '01.01.1979', 11),
(5, '3 Series', '01.01.1975', 4),
(5, '7 Series', '01.01.1977', 3),
(6, 'E-Class', '01.01.1993', 3),
(6, 'A-Class', '01.01.1997', 1),
(7, 'MX-5', '01.01.1989', 7),
(7, 'RX-7', '01.01.1978', 2),
(8, 'Ghibli', '01.01.1967', 3);

INSERT 
INTO models_sales_markets_relation (model_id, sales_market_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(2, 1),
(2, 2),
(2, 4),
(2, 5),
(3, 1),
(3, 2),
(3, 4),
(4, 1),
(4, 3),
(5, 1),
(5, 4),
(6, 1),
(6, 2),
(6, 4),
(6, 5),
(7, 1),
(7, 2),
(7, 3),
(7, 4),
(7, 5),
(7, 7),
(8, 1),
(8, 2),
(8, 3),
(8, 4),
(8, 5),
(8, 7),
(9, 1),
(9, 2),
(9, 5),
(10, 1),
(10, 2),
(10, 4),
(10, 5),
(11, 1),
(11, 2),
(11, 4),
(11, 5),
(12, 1),
(12, 2),
(12, 5),
(12, 6),
(12, 7),
(13, 5),
(13, 6),
(14, 1),
(14, 2),
(14, 4),
(14, 5),
(15, 1),
(15, 4),
(15, 5),
(16, 1),
(16, 2),
(16, 5),
(17, 1),
(17, 2),
(18, 1),
(18, 3),
(18, 4),
(18, 5),
(18, 6),
(18, 7),
(19, 3),
(19, 4),
(20, 1),
(20, 2),
(20, 5);
