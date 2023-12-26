# DataBases_MAI

Этот репозиторий хранит в себе решения лабораторных работ и курсовой по дисциплине "Базы данных" в МАИ

## Лабораторные работы:
Постановка задачи: разработать и реализовать БД по заданию (рекомендуемая СУБД – PostgreSQL)

Задание: Автомобильный журнал (сведения об авто и их производителях)
 
Основные требования:
- Наличие связи многие-ко-многим
- Таблица с количеством полей > 5

Отчёт по лабораторным работам: 
1. Описать включенные в БД таблицы (типы данных полей, default значения и т.п.), описать первичные и внешние ключи.

2. Выполнить запросы:

В отчёте при описании каждого запроса приводится:
•	назначение запроса, 
•	SQL – запрос,
•	результат выборки для заданного заполнения БД.

Типы запросов:
- использующие реляционные и булевы операторы в предикатах;
- с использованием операторов IN, BETWEEN, LIKE в условиях;
- с использованием групповых (агрегирующих) функций;
- на вычислимое поле с форматированием результата;
- с использованием нескольких таблиц;
- с использованием вложенных запросов;
- на связанные подзапросы;
- с использованием оператора JOIN;
- с использованием операторов EXIST, ANY, ALL, SOME;
- с использованием операторов UNION, INTERSECT, EXCEPT;
- с использованием оператора GROUP BY;
- с использованием оператора ORDER BY;
- с использованием выражения CASE;
- с командами обновления.

[Создание БД](https://github.com/RoKivals/DataBases_MAI/blob/main/bd.sql)

[Отчёт по ЛР](https://github.com/RoKivals/DataBases_MAI/blob/main/LR.md) 

## Курсовой проект:
Задание: Создание GUI-оболочки для БД, используемой в лабораторных работах (допускаются дополнительные правки и изменения)

Реализация: 
- GUI-оболочка написана на PyQT
- Взаимодействие с БД производится с помощью `psycopg2`

