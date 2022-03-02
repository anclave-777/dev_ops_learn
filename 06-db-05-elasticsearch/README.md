# Домашнее задание к занятию "6.5. Elasticsearch"

## Задача 1

В этом задании вы потренируетесь в:
- установке elasticsearch
- первоначальном конфигурировании elastcisearch
- запуске elasticsearch в docker

Используя докер образ [centos:7](https://hub.docker.com/_/centos) как базовый и 
[документацию по установке и запуску Elastcisearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html):

- составьте Dockerfile-манифест для elasticsearch
- соберите docker-образ и сделайте `push` в ваш docker.io репозиторий
- запустите контейнер из получившегося образа и выполните запрос пути `/` c хост-машины

Требования к `elasticsearch.yml`:
- данные `path` должны сохраняться в `/var/lib`
- имя ноды должно быть `netology_test`

В ответе приведите:
- текст Dockerfile манифеста
- ссылку на образ в репозитории dockerhub
- ответ `elasticsearch` на запрос пути `/` в json виде

Подсказки:
- возможно вам понадобится установка пакета perl-Digest-SHA для корректной работы пакета shasum
- при сетевых проблемах внимательно изучите кластерные и сетевые настройки в elasticsearch.yml
- при некоторых проблемах вам поможет docker директива ulimit
- elasticsearch в логах обычно описывает проблему и пути ее решения

Далее мы будем работать с данным экземпляром elasticsearch.

Ответ:

текст Dockerfile манифеста:

```
FROM centos:7

ADD https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz /
ADD https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 /

RUN yum update -y && \
  yum install perl-Digest-SHA -y && \
  shasum -a 512 -c elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 && \
  tar -xzf elasticsearch-7.13.4-linux-x86_64.tar.gz && \
  cd elasticsearch-7.13.4/ && \
  useradd elasticuser && \
  chown -R elasticuser:elasticuser /elasticsearch-7.13.4/ && \
  rm -rf /elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 /elasticsearch-7.13.4-linux-x86_64.tar.gz

RUN mkdir /var/lib/{data,logs} && \
  chown -R elasticuser:elasticuser /var/lib/data && \
  chown -R elasticuser:elasticuser /var/lib/logs

WORKDIR /elasticsearch-7.13.4

RUN mkdir snapshots && \
  chown -R elasticuser:elasticuser snapshots

COPY elasticsearch.yml /elasticsearch-7.13.4/config/

RUN chown -R elasticuser:elasticuser /elasticsearch-7.13.4/config

USER elasticuser

EXPOSE 9200 9300

CMD ["./bin/elasticsearch", "-Ecluster.name=netology_cluster", "-Enode.name=netology_test"]
```

Конф файл эластика:

```
root@vagrant:/home/vagrant/dockerfiles# cat elasticsearch.yml 
# ======================== Elasticsearch Configuration =========================
#
# NOTE: Elasticsearch comes with reasonable defaults for most settings.
#       Before you set out to tweak and tune the configuration, make sure you
#       understand what are you trying to accomplish and the consequences.
#
# The primary way of configuring a node is via this file. This template lists
# the most important settings you may want to configure for a production cluster.
#
# Please consult the documentation for further information on configuration options:
# https://www.elastic.co/guide/en/elasticsearch/reference/index.html
#
# ---------------------------------- Cluster -----------------------------------
#
# Use a descriptive name for your cluster:
#
#cluster.name: my-application
#
# ------------------------------------ Node ------------------------------------
#
# Use a descriptive name for the node:
#
#node.name: node-1
#
# Add custom attributes to the node:
#
#node.attr.rack: r1
#
# ----------------------------------- Paths ------------------------------------
#
# Path to directory where to store the data (separate multiple locations by comma):
#
path.data: /var/lib/data
#
# Path to log files:
#
path.logs: /var/lib/logs
#
# Path to backups
#
path.repo: /elasticsearch-7.13.4/snapshots
#
# ----------------------------------- Memory -----------------------------------
#
# Lock the memory on startup:
#
#bootstrap.memory_lock: true
#
# Make sure that the heap size is set to about half the memory available
# on the system and that the owner of the process is allowed to use this
# limit.
#
# Elasticsearch performs poorly when the system is swapping the memory.
#
# ---------------------------------- Network -----------------------------------
#
# By default Elasticsearch is only accessible on localhost. Set a different
# address here to expose this node on the network:
#
network.host: 0.0.0.0
#
# By default Elasticsearch listens for HTTP traffic on the first free port it
# finds starting at 9200. Set a specific HTTP port here:
#
#http.port: 9200
#
# For more information, consult the network module documentation.
#
# --------------------------------- Discovery ----------------------------------
#
# Pass an initial list of hosts to perform discovery when this node is started:
# The default list of hosts is ["127.0.0.1", "[::1]"]
#
discovery.seed_hosts: ["127.0.0.1", "[::1]"]
#
# Bootstrap the cluster using an initial set of master-eligible nodes:
#
#cluster.initial_master_nodes: ["node-1", "node-2"]
cluster.initial_master_nodes: ["netology_test"]
#
# For more information, consult the discovery and cluster formation module documentation.
#
# ---------------------------------- Various -----------------------------------
#
# Require explicit names when deleting indices:
#
#action.destructive_requires_name: true
```

- ссылку на образ в репозитории dockerhub
```
https://hub.docker.com/repository/docker/anclave777/test_elastic
```


- ответ `elasticsearch` на запрос пути `/` в json виде

```

root@vagrant:/home/vagrant/dockerfiles# docker push  anclave777/test_elastic:latest
The push refers to repository [docker.io/anclave777/test_elastic]
b5e3a884bae5: Pushed 
a017af42b022: Pushed 
dfd00e344fa4: Pushed 
d56603f0b4dd: Pushed 
e7542514d3cb: Pushed 
c6d0e7b12329: Layer already exists 
22a9e71a628d: Layer already exists 
174f56854903: Layer already exists 
latest: digest: sha256:7cbc7ffd91de788ab4e58e869eaec90bfc4f213a5256b576f8c32fb8ab825a31 size: 1992
root@vagrant:/home/vagrant/dockerfiles# docker ps
CONTAINER ID   IMAGE                            COMMAND                  CREATED         STATUS         PORTS                NAMES
0ddbad6ca1ae   anclave777/test_elastic:latest   "./bin/elasticsearch…"   7 seconds ago   Up 6 seconds   9200/tcp, 9300/tcp   elastic-27
root@vagrant:/home/vagrant/dockerfiles# docker exec -it 0ddbad6ca1ae /bin/bash
[elasticser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X localhost:9200
curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X GET localhost:9200
{
  "name" : "netology_test",
  "cluster_name" : "netology_cluster",
  "cluster_uuid" : "nfiMQOU4RR6TEf097UfH-Q",
  "version" : {
    "number" : "7.13.4",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "c5f60e894ca0c61cdbae4f5a686d9f08bcefc942",
    "build_date" : "2021-07-14T18:33:36.673943207Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ 

```


## Задача 2

В этом задании вы научитесь:
- создавать и удалять индексы
- изучать состояние кластера
- обосновывать причину деградации доступности данных

Ознакомтесь с [документацией](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html) 
и добавьте в `elasticsearch` 3 индекса, в соответствии со таблицей:

| Имя | Количество реплик | Количество шард |
|-----|-------------------|-----------------|
| ind-1| 0 | 1 |
| ind-2 | 1 | 2 |
| ind-3 | 2 | 4 |

Получите список индексов и их статусов, используя API и **приведите в ответе** на задание.

Получите состояние кластера `elasticsearch`, используя API.

Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?

Удалите все индексы.

**Важно**

При проектировании кластера elasticsearch нужно корректно рассчитывать количество реплик и шард,
иначе возможна потеря данных индексов, вплоть до полной, при деградации системы.

**Ответ**

Добавляем:

```
curl -X PUT "localhost:9200/ind-1" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 1,  
      "number_of_replicas": 0 
    }
  }
}
'

curl -X PUT "localhost:9200/ind-2" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 2,  
      "number_of_replicas": 1 
    }
  }
}
'

curl -X PUT "localhost:9200/ind-3" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 4,  
      "number_of_replicas": 2 
    }
  }
}
'
```

Список индексов:

```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X GET "localhost:9200/_cat/indices?v"
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   ind-1 un4BxryuTPSngYnsxs0gRw   1   0          0            0       208b           208b
yellow open   ind-3 GtiXl8hQSgWe1_4DfpvLBg   4   2          0            0       832b           832b
yellow open   ind-2 fQ-ZnEMBQFWRpWvplRfe0A   2   1          0            0       416b           416b
```

Состояние кластера через апи:

```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X GET "localhost:9200/_cluster/health?pretty"
{
  "cluster_name" : "netology_cluster",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 7,
  "active_shards" : 7,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 41.17647058823529
}
```

Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?:

```
Состояние Yellow говорит о том, что у индексов ind-2 и ind-3 данные должны быть реплицированы на
другие узелы, ведь указаны реплики больше 0
```

Удаляем индексы

```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X DELETE "localhost:9200/_all"
{"acknowledged":true}[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ 
```

## Задача 3

В данном задании вы научитесь:
- создавать бэкапы данных
- восстанавливать индексы из бэкапов

Создайте директорию `{путь до корневой директории с elasticsearch в образе}/snapshots`.

Используя API [зарегистрируйте](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-register-repository.html#snapshots-register-repository) 
данную директорию как `snapshot repository` c именем `netology_backup`.

**Приведите в ответе** запрос API и результат вызова API для создания репозитория.

Создайте индекс `test` с 0 реплик и 1 шардом и **приведите в ответе** список индексов.

[Создайте `snapshot`](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-take-snapshot.html) 
состояния кластера `elasticsearch`.

**Приведите в ответе** список файлов в директории со `snapshot`ами.

Удалите индекс `test` и создайте индекс `test-2`. **Приведите в ответе** список индексов.

[Восстановите](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-restore-snapshot.html) состояние
кластера `elasticsearch` из `snapshot`, созданного ранее. 

**Приведите в ответе** запрос к API восстановления и итоговый список индексов.

Подсказки:
- возможно вам понадобится доработать `elasticsearch.yml` в части директивы `path.repo` и перезапустить `elasticsearch`

---


Ответ:

Приведите в ответе запрос API и результат вызова API для создания репозитория.

```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X PUT "localhost:9200/_snapshot/netology_backup" -H 'Content-Type: application/json' -d'
> {
>   "type": "fs",
>   "settings": {
>     "location": "/elasticsearch-7.13.4/snapshots"
>   }
> }
> {
>   "acknowledged" : true
> }
> 
> '
{"acknowledged":true}[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ 
```


Создайте индекс `test` с 0 реплик и 1 шардом и **приведите в ответе** список индексов.


```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X GET "localhost:9200/_cat/indices?v"
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test  pbnsqJUxS1u3fgrkOEIQsg   1   0          0            0       208b           208b
```

**Приведите в ответе** список файлов в директории со `snapshot`ами.


```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$ curl -X PUT "localhost:9200/_snapshot/netology_backup/snapshot_1?wait_for_completion=true&pretty"
{
  "snapshot" : {
    "snapshot" : "snapshot_1",
    "uuid" : "6dTVR7_GRYCFn51YEYij5w",
    "version_id" : 7130499,
    "version" : "7.13.4",
    "indices" : [
      "test"
    ],
    "data_streams" : [ ],
    "include_global_state" : true,
    "state" : "SUCCESS",
    "start_time" : "2021-11-22T00:07:14.552Z",
{
  "snapshot" : {
    "snapshot" : "snapshot_1",
    "uuid" : "9oiSqm0qTim2f-bQ3sbG0g",
    "version_id" : 7130499,
    "version" : "7.13.4",
    "indices" : [
      "test"
    ],
    "data_streams" : [ ],
    "include_global_state" : true,
    "state" : "SUCCESS",
    "start_time" : "2022-02-28T19:55:32.295Z",
    "start_time_in_millis" : 1646078132295,
    "end_time" : "2022-02-28T19:55:32.295Z",
    "end_time_in_millis" : 1646078132295,
    "duration_in_millis" : 0,
    "failures" : [ ],
    "shards" : {
      "total" : 1,
      "failed" : 0,
      "successful" : 1
    },
    "feature_states" : [ ]
  }
}
```


**Приведите в ответе** список файлов в директории со `snapshot`ами.


```
root@vagrant:/home/vagrant# docker ps
CONTAINER ID   IMAGE                            COMMAND                  CREATED        STATUS        PORTS                NAMES
0ddbad6ca1ae   anclave777/test_elastic:latest   "./bin/elasticsearch…"   22 hours ago   Up 22 hours   9200/tcp, 9300/tcp   elastic-27
root@vagrant:/home/vagrant# docker exec -it elastic-27 ls /elasticsearch-7.13.4/snapshots       
index-0       indices                          snap-9oiSqm0qTim2f-bQ3sbG0g.dat
index.latest  meta-9oiSqm0qTim2f-bQ3sbG0g.dat
root@vagrant:/home/vagrant# 
```



Удалите индекс `test` и создайте индекс `test-2`. **Приведите в ответе** список индексов.


```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$curl -X DELETE "localhost:9200/test"
{"acknowledged":true}

[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$curl -X PUT "localhost:9200/test-2?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 1,  
      "number_of_replicas": 0 
    }
  }
}
'
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test-2"
}

[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$curl -X GET "localhost:9200/_cat/indices?v"
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 3h9iC93NTXqYQIGhgPvWkw   1   0          0            0       208b           208b
```

**Приведите в ответе** запрос к API восстановления и итоговый список индексов.

```
[elasticuser@0ddbad6ca1ae elasticsearch-7.13.4]$curl -X POST "localhost:9200/_snapshot/netology_backup/snapshot_1/_restore?pretty"
{
  "accepted" : true
}

curl -X GET "localhost:9200/_cat/indices?v"
health status index  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test-2 3h9iC93NTXqYQIGhgPvWkw   1   0          0            0       208b           208b
green  open   test   JmT0WCeGRB2OskyiD1PHAw   1   0          0            0       208b           208b

```



### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
