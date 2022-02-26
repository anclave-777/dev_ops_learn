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

## Задача 4

Используя утилиту `pg_dump` создайте бекап БД `test_database`.

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца `title` для таблиц `test_database`?

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
