# Запросы к базе данных "Автомобильный журнал"

## Реляционные и булевы операторы

Запрос 1:
- Назначение: Узнать компании, в которых количество работников меньше 100К человек
- Запрос: 
```sql 
SELECT * from companies where count_of_workers < 100000
```
- Результат: 

Запрос 2:
- Назначение: Узнать компании, в которых количество работников больше 100К человек и они были образованы после конца первой мировой войны
- Запрос: 
```sql 
SELECT * from companies where count_of_workers > 100000 AND creation_date > '11.11.1918'
```
- Результат: 

Запрос 3:
- Назначение: Узнать компании, в которых количество работников не меньше 50К человек, а также головной офис и завод компании находятся в одном городе
- Запрос: 
```sql 
SELECT * from companies where NOT count_of_workers < 50000 AND office = factory
```
- Результат: 

## Операторы `IN` `BETWEEN` `LIKE`

Запрос 1:
- Назначение: Узнать компании, головной офис, которых находится в одном из перечисленных городов
- Запрос: 
```sql 
SELECT * from companies where office IN ('Wolfsburg', 'Las Vegas', 'Moscow')
```
- Результат: 

Запрос 2:
- Назначение: Узнать компании, в которых количество работников находится в диапазоне между двух значений
- Запрос: 
```sql 
SELECT * from companies where count_of_workers BETWEEN 80000 AND 500000
```
- Результат: 

Запрос 3:
- Назначение: Узнать модели автомобилей, название которых начинается с буквы A
- Запрос: 
```sql 
SELECT * from models where name LIKE 'A%'
```
- Результат: 

## Агрегирующие функции

Запрос 1:
- Назначение: Посчитать количество моделей Audi начинающихся с буквы A
- Запрос: 
```sql 
SELECT count(id) from models 
where name LIKE 'A%' 
AND models.company_id = (select id from companies where name = 'Audi')
```
- Результат: 

Запрос 2:
- Назначение: Узнать среднее количество работников среди компаний с головным офисов в определённых городах
- Запрос: 
```sql 
SELECT AVG(count_of_workers) from companies where office IN ('Munich', 'Hiroshima', 'Zuffenhausen')
```
- Результат: 

Запрос 3:
- Назначение: Узнать название компании с минимальным количество работников
- Запрос: 
```sql 
SELECT name from companies where count_of_workers = (select MIN(count_of_workers) from companies)
```
- Результат: 

## Форматирование результата

Запрос 1:
- Назначение: Вывести названия моделей вместе с названием их бренда
- Запрос: 
```sql 
SELECT FORMAT('%s %s', companies.name, models.name) from models 
JOIN companies ON models.company_id = companies.id
```
- Результат: 

Запрос 2:
- Назначение: Вывести название компании и год её основания (только год)
- Запрос: 
```sql 
SELECT name as company, extract(year from creation_date) AS foundation_year from companies
```
- Результат: 

Запрос 3:
- Назначение: Вывести название компании и дату её основания в формате `ГГГГ-Мес`
- Запрос: 
```sql 
SELECT name as company, TO_CHAR(creation_date, 'YYYY-Mon') AS foundation_date from companies
```
- Результат: 


## Несколько таблиц в запросе
	  
Запрос 1:
- Назначение: Вывести названия моделей и названия рынков, на которых они продаются
- Запрос: 
```sql 
SELECT models.name, sales_markets.market_zone from models, sales_markets, models_sales_markets_relation
WHERE (models.id = models_sales_markets_relation.model_id
	  AND sales_markets.id = models_sales_markets_relation.sales_market_id)
```
- Результат: 

Запрос 2:
- Назначение: Вывести названия моделей вместе с названием их бренда
- Запрос: 
```sql 
SELECT companies.name, models.name from models, companies
WHERE companies.id = models.company_id
```
- Результат: 

Запрос 3:
- Назначение: Вывести название компании и год релиза её самой ранней модели (из БД)
- Запрос: 
```sql 
SELECT companies.name, MIN(extract(year from models.release_date))
from companies, models
where companies.id = models.company_id
GROUP BY companies.name
```
- Результат: 

## Вложенные запросы

Запрос 1:
- Назначение: Узнать название компании с минимальным количество работников
- Запрос: 
```sql 
SELECT name from companies where count_of_workers = (select MIN(count_of_workers) from companies)
```
- Результат: 

Запрос 2:
- Назначение: Вывести названия компаний и кол-во работников, где их количество больше среднего значения работников среди всех компаний
- Запрос: 
```sql 
SELECT name, count_of_workers from companies 
where count_of_workers > (select AVG(count_of_workers) from companies)
```
- Результат: 

Запрос 3:
- Назначение: Вывести название моделей, которые были представлены спустя 70 лет после основания компании производителя
- Запрос: 
```sql 
SELECT models.name from models
where models.release_date - (SELECT creation_date from companies 
							 where companies.id = models.company_id) > 364 * 70
```
- Результат: 

## Связанные подзапросы

Запрос 1:
- Назначение: Вывести компании и рынки сбыта, в которых у этой компании представлено наибольшее количество моделей 
- Запрос: 
```sql 
WITH companies_markets AS (SELECT companies.name, market_zone, COUNT(market_zone) as market_models from companies JOIN models
ON models.company_id = companies.id
JOIN models_sales_markets_relation
ON models.id = models_sales_markets_relation.model_id
JOIN sales_markets
ON sales_markets.id = models_sales_markets_relation.sales_market_id
GROUP BY companies.name, market_zone
ORDER BY companies.name)

SELECT name, market_zone from companies_markets CM1 where 
market_models = (SELECT MAX(market_models) from companies_markets CM2 WHERE CM1.name = CM2.name)
```
- Результат: 


## Оператор JOIN

Запрос 1:
- Назначение: Полная информация о модели и компании, которой она принадлежит
- Запрос: 
```sql 
SELECT * from companies JOIN models ON models.company_id = companies.id
```
- Результат:

Запрос 2:
- Назначение: Вывод названия моделей и их рынков сбыта
- Запрос: 
```sql 
SELECT models.name, market_zone from models JOIN models_sales_markets_relation
ON models.id = models_sales_markets_relation.model_id
JOIN sales_markets ON sales_markets.id = models_sales_markets_relation.sales_market_id
```
- Результат: 

Запрос 3:
- Назначение: Вывести компании и кол-во представленных ими моделей на каждом из рынков сбыта
- Запрос: 
```sql 
WITH companies_markets AS (SELECT companies.name, market_zone, COUNT(market_zone) as market_models from companies JOIN models
ON models.company_id = companies.id
JOIN models_sales_markets_relation
ON models.id = models_sales_markets_relation.model_id
JOIN sales_markets
ON sales_markets.id = models_sales_markets_relation.sales_market_id
GROUP BY companies.name, market_zone
ORDER BY companies.name)

SELECT * from companies_markets
```
- Результат:

## Операторы `EXIST` `ANY` `ALL` `SOME`

Запрос 1:
- Назначение: Полная информация о моделях и рынках сбыта, если среди моделей есть названия начинающиеся с A
- Запрос: 
```sql 
WITH models_markets AS (SELECT * from models 
JOIN models_sales_markets_relation
ON models.id = models_sales_markets_relation.model_id)

SELECT * from models_markets 
where EXISTS(select * 
			  from models_markets 
			where name LIKE 'A%')

```
- Результат:

Запрос 2:
- Назначение: Вывод информации о моделях, продаваемых на азиатском рынке (включая Китай)
- Запрос: 
```sql 
WITH models_markets AS (SELECT * from models 
JOIN models_sales_markets_relation
ON models.id = models_sales_markets_relation.model_id)

SELECT * from models_markets 
where sales_market_id = ANY(select id from sales_markets
						   where market_zone IN ('Asia', 'China'))
```
- Результат: 

Запрос 3:
- Назначение: Вывести компании, которые были созданы позже ВСЕХ компаний, кол-во сотрудников которых не более 100К
- Запрос: 
```sql 
SELECT name from companies
where creation_date > 
ALL(SELECT creation_date from companies where count_of_workers <= 100000)
```
- Результат:

Запрос 4:
- Назначение: Вывести модели, которые произведены компаниями с количеством работников не более 100К
- Запрос: 
```sql 
SELECT name from models
where company_id =  
SOME(SELECT id from companies where count_of_workers <= 100000)
```
- Результат:

## Операторы `UNION` `INTERSECT` `EXCEPT`

## Оператор `GROUP BY`

Запрос 1:
- Назначение: Количество моделей для каждого типа кузова
- Запрос: 
```sql 
SELECT body_type.name, COUNT(*) from models
JOIN body_type ON models.body_type = body_type.id
GROUP BY body_type.name
```
- Результат:

Запрос 2:
- Назначение: Количество моделей у каждой компании
- Запрос: 
```sql 
SELECT companies.name, count(models.id) from models JOIN companies
ON models.company_id = companies.id
GROUP by companies.name
```
- Результат: 

Запрос 3:
- Назначение: Город в котором находится завод и максимальное кол-во работников компании, завод которой находится в этом городе
- Запрос: 
```sql 
SELECT factory, MAX(count_of_workers) from models JOIN companies
ON models.company_id = companies.id
GROUP BY factory
```
- Результат:

## Оператор `ORDER BY`

Запрос 1:
- Назначение: Отсортировать компании от новых к старым
- Запрос: 
```sql 
SELECT * from companies
ORDER BY creation_date DESC
```
- Результат:

Запрос 2:
- Назначение: Отсортировать компании по количеству работников по убыванию
- Запрос: 
```sql 
SELECT * from companies
ORDER BY count_of_workers DESC
```
- Результат:

Запрос 3:
- Назначение: Отсортировать модели в алфавитном порядке их названия
- Запрос: 
```sql 
SELECT * from models
ORDER BY name
```
- Результат:

## Выражение `CASE`

## Команды `UPDATE` `INSERT` `DELETE`