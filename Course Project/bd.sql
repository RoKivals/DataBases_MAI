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
);

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
	generation varchar(55),
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
);

CREATE FUNCTION set_model_body_type_relation_function()
RETURNS TRIGGER AS 
$$
BEGIN
    INSERT INTO model_body_type_relation (model_id, body_type_id) VALUES (NEW.model_id, NEW.body_type);
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER model_body_type_relation_insert
AFTER INSERT ON specification
FOR EACH ROW
EXECUTE FUNCTION set_model_body_type_relation_function();


CREATE UNIQUE INDEX IF NOT EXISTS uix_companies_name ON companies (name);
CREATE UNIQUE INDEX IF NOT EXISTS uix_body_type_name ON body_type (name);
CREATE UNIQUE INDEX IF NOT EXISTS uix_model_name ON models_range (model_name);
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
('Acura', 'Torrance', '27.03.1986', 23805),
('Alfa Romeo', 'Turin', '24.06.1910', 3000),
('Aston Martin', 'Warwick', '15.01.1913', 2473),
('Audi', 'Ingolstadt', '16.07.1909', 87000),
('Bentley', 'Crewe', '18.01.1919', 3600),
('BMW', 'Munich', '07.03.1916', 118909),
('Bugatti', 'Molsheim', '01.01.1909', 1100),
('BYD', 'Shaanxi Province', '10.02.1995', 288200),
('Cadillac', 'Detroit', '22.08.1902', 11000),
('Chevrolet', 'Detroit', '03.11.1911', 20000),
('Crysler', 'Auburn Hills', '06.06.1925', 56900),
('Citroen', 'Poissy', '04.06.1919', 197000),
('Dacia', 'Mioveni', '01.09.1966', 12209),
('Dodge', 'Auburn Hills', '14.12.1900', 235000),
('Ferrari', 'Maranello', '13.09.1939', 4571),
('Fiat', 'Turin', '11.07.1899', 214836),
('Ford', 'Las Vegas', '16.06.1903', 183000),
('Haval', 'Baoding', '29.03.2013', 25000),
('Honda', 'Tokyo', '24.09.1948', 197039),
('Hummer', 'Detroit', '22.01.1992', 1000),
('Infiniti', 'Yokohama', '08.11.1989', 8000),
('Jeep', 'Auburn Hills', '01.01.1941', 7500),
('KIA', 'Seoul', '21.12.1944', 51975),
('Lada', 'Tolyatti', '20.07.1966', 32500),
('Lamborghini', 'Sant''Agata Bolognese', '30.10.1963', 1779),
('Lexus', 'Nagoya', '01.09.1989', 70000),
('Lotus', 'Hethel', '01.01.1952', 1385),
('Maserati', 'Modena', '01.12.1914', 1100),
('Mazda', 'Hiroshima', '30.01.1920', 49786),
('Mercedes-Benz', 'Stuttgart', '28.06.1926', 145436),
('Mini', 'Farnborough', '01.04.1952', 14000),
('Pagani', 'San Cesario sul Panaro', '01.01.1992', 162),
('Porsche', 'Stuttgart', '06.03.1931', 36359),
('Rolls-Royce', 'Goodwood', '01.03.1998', 1300),
('Skoda', 'Mladá Boleslav', '17.12.1895', 36032),
('Subaru', 'Shibuya', '15.07.1953', 16961),
('Tesla', 'Austin', '01.07.2003', 127855),
('Toyota', 'Koromo', '28.08.1937', 366283),
('Volkswagen', 'Wolfsburg', '28.05.1937', 670000);

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['CSX', 'Integra', 'MDX', 'NSX']) from companies where name = 'Acura';

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['Bulldog', 'DB11', 'DB12', 'DBS', 'One-77']) from companies where name = 'Aston Martin';

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['80', '100', '200', 'A4', 'A6', 'A7', 'A8', 'Q8', 'R8', 'RS6']) from companies where name = 'Audi';

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['Series 1', 'Series 3', 'Series 5', 'Series 7', 'i8', 'Isetta', 'M6', 'M8', 'X5', 'Z4']) 
from companies where name = 'BMW';

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['300 SLR', 'AMG GT', 'C Class', 'CLA', 'E Class', 'EQB', 'G Class', 'GLS', 'S Class', 'W124']) 
from companies where name = 'Mercedes-Benz';

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['356', '718', '911', '918', '959', 'Boxster', 'Cayenne', 'Cayman', 'Macan', 'Taycan']) 
from companies where name = 'Porsche';

INSERT INTO models_range(company_id, model_name) VALUES
SELECT id, UNNEST (ARRAY['Amarok', 'Arteon', 'Beetle', 'Bora', 'Caddy', 'Golf', 'ID.7', 'Jetta', 'Passat', 'Touareg']) 
from companies where name = 'Volkswagen';

WITH model AS (SELECT id from models_range WHERE model_name = 'NSX')
INSERT INTO 
specification(model_id, generation, start_of_production, end_of_production, engine, engine_displacement, HP, body_type) VALUES
(model.id, 'NSX II', '01.01.2022', NULL, 'hybrid', 3493, 520, 2);

WITH model AS (SELECT id from models_range WHERE model_name = 'DBS')
INSERT INTO 
specification(model_id, generation, start_of_production, end_of_production, engine, engine_displacement, HP, body_type) VALUES
(model.id, 'NSX II', '01.01.2022', NULL, 'hybrid', 3493, 520, 2);
