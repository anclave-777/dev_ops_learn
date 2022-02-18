# Домашнее задание к занятию "6.2. SQL"

## Введение

Перед выполнением задания вы можете ознакомиться с 
[дополнительными материалами](https://github.com/netology-code/virt-homeworks/tree/master/additional/README.md).

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, 
в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.

Ответ:

```
root@vagrant:/home/vagrant/dockerfiles# cat docker-compose.yml 
version: "3.1"

services:
  pgdb_1:
    image: postgres:12
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret
      - ALLOW_EMPTY_PASSWORD=yes
    volumes:
      - "/var/snap/docker/common/var-lib-docker/volumes/pgsql/_data:/var/lib/postgresql/data"
      - "/var/snap/docker/common/var-lib-docker/volumes/pgsql_backup/_data:/var/lib/postgresql/backups"
    ports:
      - "5432:5432"
      
```

## Задача 2

В БД из задачи 1: 
- создайте пользователя test-admin-user и БД test_db

```

root@69771499ab07:/# psql --u postgres
psql (12.10 (Debian 12.10-1.pgdg110+1))
Type "help" for help.

postgres=# CREATE USER "test-admin-user" WITH PASSWORD 'test-admin-user';
CREATE ROLE
postgres=# CREATE DATABASE test_db;

```

- в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)




- предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
- создайте пользователя test-simple-user  
- предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db

Таблица orders:
- id (serial primary key)
- наименование (string)
- цена (integer)


Таблица clients:
- id (serial primary key)
- фамилия (string)
- страна проживания (string, index)
- заказ (foreign key orders)


```
test_db=# CREATE TABLE orders (
test_db(#     id integer PRIMARY KEY,
test_db(#     name varchar(128),
test_db(#     price numeric(10,2)
test_db(# );

CREATE TABLE clients (
CREATE TABLE
test_db=# 
test_db=# CREATE TABLE clients (
test_db(#     id integer PRIMARY KEY,
test_db(#     fio varchar(64),
test_db(#     country varchar(64),
test_db(#     order_id integer default null,
test_db(#     FOREIGN KEY (order_id) REFERENCES orders (id)
test_db(# );
CREATE TABLE

```


```
test_db=# GRANT ALL PRIVILEGES ON orders TO "test-admin-user";
GRANT
test_db=# GRANT ALL PRIVILEGES ON clients TO "test-admin-user";
GRANT
```

```
test_db=# CREATE USER "test-simple-user" WITH PASSWORD 'test-simple-user';
CREATE ROLE
test_db=# GRANT SELECT, INSERT, UPDATE, DELETE ON orders TO "test-simple-user";
GRANT
test_db=# GRANT SELECT, INSERT, UPDATE, DELETE ON clients TO "test-simple-user";
```


Приведите:
- итоговый список БД после выполнения пунктов выше,
- описание таблиц (describe)
- SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
- список пользователей с правами над таблицами test_db


```
postgres=# \c test_db                   
You are now connected to database "test_db" as user "postgres".
test_db=# \list
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

test_db=#

```

```
test_db=# \d orders
                      Table "public.orders"
 Column |          Type          | Collation | Nullable | Default 
--------+------------------------+-----------+----------+---------
 id     | integer                |           | not null | 
 name   | character varying(128) |           |          | 
 price  | numeric(10,2)          |           |          | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_order_id_fkey" FOREIGN KEY (order_id) REFERENCES orders(id)

test_db=# \d clients
                      Table "public.clients"
  Column  |         Type          | Collation | Nullable | Default 
----------+-----------------------+-----------+----------+---------
 id       | integer               |           | not null | 
 fio      | character varying(64) |           |          | 
 country  | character varying(64) |           |          | 
 order_id | integer               |           |          | 
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "clients_order_id_fkey" FOREIGN KEY (order_id) REFERENCES orders(id)

test_db=# 
```

```
test_db=# SELECT * FROM information_schema.table_privileges
test_db-# WHERE table_catalog = 'test_db'
test_db-#   AND table_schema = 'public'
test_db-#   AND grantee != 'postgres';
 grantor  |     grantee      | table_catalog | table_schema | table_name | privilege_type
 | is_grantable | with_hierarchy 
----------+------------------+---------------+--------------+------------+---------------
-+--------------+----------------
 postgres | test-admin-user  | test_db       | public       | orders     | INSERT        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | SELECT        
 | NO           | YES
 postgres | test-admin-user  | test_db       | public       | orders     | UPDATE        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | DELETE        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | TRUNCATE      
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | REFERENCES    
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | orders     | TRIGGER       
 | NO           | NO
 postgres | test-simple-user | test_db       | public       | orders     | INSERT        
 | NO           | NO
 postgres | test-simple-user | test_db       | public       | orders     | SELECT        
 | NO           | YES
 postgres | test-simple-user | test_db       | public       | orders     | UPDATE        
 | NO           | NO
 postgres | test-simple-user | test_db       | public       | orders     | DELETE        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | INSERT        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | SELECT        
 | NO           | YES
 postgres | test-admin-user  | test_db       | public       | clients    | UPDATE        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | DELETE        
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | TRUNCATE      
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | REFERENCES    
 | NO           | NO
 postgres | test-admin-user  | test_db       | public       | clients    | TRIGGER       
 | NO           | NO
 postgres | test-simple-user | test_db       | public       | clients    | INSERT        
 | NO           | NO
 postgres | test-simple-user | test_db       | public       | clients    | SELECT        
 | NO           | YES
 postgres | test-simple-user | test_db       | public       | clients    | UPDATE        
 | NO           | NO
 postgres | test-simple-user | test_db       | public       | clients    | DELETE        
 | NO           | NO
(22 rows)
```



## Задача 3

Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders

|Наименование|цена|
|------------|----|
|Шоколад| 10 |
|Принтер| 3000 |
|Книга| 500 |
|Монитор| 7000|
|Гитара| 4000|

Таблица clients

|ФИО|Страна проживания|
|------------|----|
|Иванов Иван Иванович| USA |
|Петров Петр Петрович| Canada |
|Иоганн Себастьян Бах| Japan |
|Ронни Джеймс Дио| Russia|
|Ritchie Blackmore| Russia|

Используя SQL синтаксис:
- вычислите количество записей для каждой таблицы 
- приведите в ответе:
    - запросы 
    - результаты их выполнения.

Ответ:

```
root@69771499ab07:/# psql --u postgres 
psql (12.10 (Debian 12.10-1.pgdg110+1))
Type "help" for help.

postgres=# \c test_db
You are now connected to database "test_db" as user "postgres".
test_db=# \d+
                      List of relations
 Schema |  Name   | Type  |  Owner   |  Size   | Description 
--------+---------+-------+----------+---------+-------------
 public | clients | table | postgres | 0 bytes | 
 public | orders  | table | postgres | 0 bytes | 
(2 rows)

test_db=# INSERT INTO orders (id, name, price) VALUES
test_db-# (1, 'Шоколад', 10),
test_db-# (2, 'Принтер', 3000),
test_db-# (3, 'Книга', 500),
test_db-# (4, 'Монитор', 7000),
test_db-# (5, 'Гитара', 4000);
INSERT 0 5
test_db=# 
test_db=# INSERT INTO clients (id, fio, country) VALUES
test_db-# (1, 'Иванов Иван Иванович', 'USA'),
test_db-# (2, 'Петров Петр Петрович', 'Canada'),
test_db-# (3, 'Иоганн Себастьян Бах', 'Japan'),
test_db-# (4, 'Ронни Джеймс Дио', 'Russia'),
test_db-# (5, 'Ritchie Blackmore', 'Russia');
INSERT 0 5
```

```
test_db=# SELECT COUNT(*) FROM orders;
 count 
-------
     5
(1 row)

test_db=# SELECT COUNT(*) FROM clients;
 count 
-------
     5
(1 row)

test_db=# 
```


## Задача 4

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.

Используя foreign keys свяжите записи из таблиц, согласно таблице:

|ФИО|Заказ|
|------------|----|
|Иванов Иван Иванович| Книга |
|Петров Петр Петрович| Монитор |
|Иоганн Себастьян Бах| Гитара |

Приведите SQL-запросы для выполнения данных операций.

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.
 
Подсказк - используйте директиву `UPDATE`.

## Задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 
(используя директиву EXPLAIN).

Приведите получившийся результат и объясните что значат полученные значения.

## Задача 6

Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).

Остановите контейнер с PostgreSQL (но не удаляйте volumes).

Поднимите новый пустой контейнер с PostgreSQL.

Восстановите БД test_db в новом контейнере.

Приведите список операций, который вы применяли для бэкапа данных и восстановления. 

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
