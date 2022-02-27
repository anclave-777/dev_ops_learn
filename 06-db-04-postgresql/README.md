# Домашнее задание к занятию "6.4. PostgreSQL"

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.

Подключитесь к БД PostgreSQL используя `psql`.


```
docker volume create --name=netology_pgdata

docker volume create --name=netology_pgbackups
```

```

version: "3.1"

services:
  pgdb_1:
    image: postgres:13
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret
      - ALLOW_EMPTY_PASSWORD=yes
    volumes:
      - pgdata:/var/lib/postgresql/data"
      - pgbackups:/var/lib/postgresql/backups
    ports:
      - "5432:5432"

volumes:
  pgdata:
    external: true
    name: netology_pgdata
  pgbackups:
    external: true
    name: netology_pgbackups
    
```


```
Status: Downloaded newer image for postgres:13
Creating dockerfiles_pgdb_1_1 ... done
root@vagrant:/home/vagrant/dockerfiles# docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS              PORTS                                                  NAMES
05ad6cb90be3   postgres:13   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp              dockerfiles_pgdb_1_1
```

```
root@vagrant:/home/vagrant/dockerfiles# docker exec -it  dockerfiles_pgdb_1_1 /bin/bash 
root@05ad6cb90be3:/# psql -U postgres
psql (13.6 (Debian 13.6-1.pgdg110+1))
Type "help" for help.

```

Воспользуйтесь командой `\?` для вывода подсказки по имеющимся в `psql` управляющим командам.

**Найдите и приведите** управляющие команды для:
- вывода списка БД
- подключения к БД
- вывода списка таблиц
- вывода описания содержимого таблиц
- выхода из psql

```
\l[+]   [PATTERN]      list databases

\c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}

\d[S+]                 list tables, views, and sequences

\d[S+]  NAME           describe table, view, sequence, or index

\q                     quit psql
```

## Задача 2

Используя `psql` создайте БД `test_database`.

```
postgres=# CREATE DATABASE test_database;
CREATE DATABASE
```

Изучите [бэкап БД](https://github.com/netology-code/virt-homeworks/tree/master/06-db-04-postgresql/test_data).

Восстановите бэкап БД в `test_database`.

```
root@05ad6cb90be3:/var/lib/postgresql/backups# ls
test_dump.sql
root@05ad6cb90be3:/var/lib/postgresql/backups# psql -U postgres -d test_database -f /var/lib/postgresql/backups/test_dump.sql
SET
SET
SET
SET
SET
 set_config 
------------
 
(1 row)

SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
ALTER TABLE
COPY 8
 setval 
--------
      8
(1 row)

ALTER TABLE
```

Перейдите в управляющую консоль `psql` внутри контейнера.

Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.

```
root@05ad6cb90be3:/var/lib/postgresql/backups# psql -U postgres
psql (13.6 (Debian 13.6-1.pgdg110+1))
Type "help" for help.

postgres=# \c test_database;
You are now connected to database "test_database" as user "postgres".
test_database=# \dt
         List of relations
 Schema |  Name  | Type  |  Owner   
--------+--------+-------+----------
 public | orders | table | postgres
(1 row)

test_database=# ANALYZE orders;
ANALYZE
test_database=# 
```


Используя таблицу [pg_stats](https://postgrespro.ru/docs/postgresql/12/view-pg-stats), найдите столбец таблицы `orders` 
с наибольшим средним значением размера элементов в байтах.

```
test_database=# SELECT MAX(avg_width) max_avg_width FROM pg_stats WHERE tablename = 'orders';
 max_avg_width 
---------------
            16
(1 row)

test_database=# 
```

**Приведите в ответе** команду, которую вы использовали для вычисления и полученный результат.

## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и
поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили
провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

```
test_database=# BEGIN TRANSACTION;
BEGIN
test_database=*# CREATE TABLE public.orders_main (
test_database(*#     id integer NOT NULL,
test_database(*#     title character varying(80) NOT NULL,
test_database(*#     price integer DEFAULT 0
test_database(*# ) PARTITION BY RANGE(price);
CREATE TABLE
test_database=*# CREATE TABLE orders_1 PARTITION OF orders_main FOR VALUES FROM (500) TO (MAXVALUE);
CREATE TABLE
test_database=*# CREATE TABLE orders_2 PARTITION OF orders_main FOR VALUES FROM (MINVALUE) TO (500);
CREATE TABLE
test_database=*# INSERT INTO orders_main SELECT * FROM orders;
INSERT 0 8
test_database=*# COMMIT;
COMMIT
test_database=# SELECT * FROM orders_main;
 id |        title         | price 
----+----------------------+-------
  1 | War and peace        |   100
  3 | Adventure psql time  |   300
  4 | Server gravity falls |   300
  5 | Log gossips          |   123
  7 | Me and my bash-pet   |   499
  2 | My little database   |   500
  6 | WAL never lies       |   900
  8 | Dbiezdmin            |   501
(8 rows)

test_database=# SELECT * FROM orders_1;
 id |       title        | price 
----+--------------------+-------
  2 | My little database |   500
  6 | WAL never lies     |   900
  8 | Dbiezdmin          |   501
(3 rows)

test_database=#  SELECT * FROM orders_2;
 id |        title         | price 
----+----------------------+-------
  1 | War and peace        |   100
  3 | Adventure psql time  |   300
  4 | Server gravity falls |   300
  5 | Log gossips          |   123
  7 | Me and my bash-pet   |   499
(5 rows)

test_database=# 
```

```
Ответ на вопрос из задания: Нельзя превратить обычную таблицу в таблицу с поддержкой разбиения.
```

## Задача 4

Используя утилиту `pg_dump` создайте бекап БД `test_database`.

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца `title` для таблиц `test_database`?

```
root@vagrant:/var/snap/docker/common/var-lib-docker/volumes/netology_pgbackups/_data# docker exec -t dockerfiles_pgdb_1_1 pg_dump -U postgres test_database -f /var/lib/postgresql/backups/test_database_2.sql
root@vagrant:/var/snap/docker/common/var-lib-docker/volumes/netology_pgbackups/_data# 
```

```
CREATE UNIQUE INDEX title_unique ON orders_main (title, price);
```

## Доработка

Альтернатива из документации на https://www.postgresql.org/
Note: The preferred way to add a unique constraint to a table is ALTER TABLE ... ADD CONSTRAINT. The use of indexes to enforce unique constraints could be considered an implementation detail that should not be accessed directly. One should, however, be aware that there's no need to manually create indexes on unique columns; doing so would just duplicate the automatically-created index.

```
ALTER TABLE orders_main
ADD CONSTRAINT title_unique  UNIQUE (title);
```

В этом примере мы создали уникальное ограничение для существующей таблицы orders_main с именем title_unique . Он состоит из поля с именем order_id.

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
