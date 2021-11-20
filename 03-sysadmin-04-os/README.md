# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

1. На лекции мы познакомились с [node_exporter](https://github.com/prometheus/node_exporter/releases). В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой [unit-файл](https://www.freedesktop.org/software/systemd/man/systemd.service.html) для node_exporter:

    * поместите его в автозагрузку,
    * предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на `systemctl cat cron`),
    * удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.
Ответ:
  ```
  Скачал wget https://github.com/prometheus/node_exporter/releases/download/v1.2.0/node_exporter-1.2.0.linux-amd64.tar.gz
  Распаковал tar xvfz node_exporter-1.2.0.linux-amd64.tar.gz
  Сделал юнит файл:
  root@vagrant:/home/vagrant# cat /etc/systemd/system/node-exporter.service      
[Unit]
Description=Node Exporter
 
[Service]
ExecStart=/home/vagrant/node_exporter-1.2.0.linux-amd64/node_exporter
 
[Install]
WantedBy=multi-user.target
Скомандовал:
root@vagrant:/home/vagrant# systemctl daemon-reload
root@vagrant:/home/vagrant# systemctl start node-exporter.service

Сервис работает.
root@vagrant:/home/vagrant# systemctl status node-exporter.service
● node-exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node-exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2021-11-19 17:34:23 UTC; 4s ago
   Main PID: 5910 (node_exporter)
      Tasks: 4 (limit: 1071)
     Memory: 2.2M
     CGroup: /system.slice/node-exporter.service
             └─5910 /home/vagrant/node_exporter-1.2.0.linux-amd64/node_exporter

Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=thermal_zone
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=time
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=timex
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=udp_queues
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=uname
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=vmstat
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=xfs
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:115 collector=zfs
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=node_exporter.go:199 msg="Listening on" address=:9100
Nov 19 17:34:23 vagrant node_exporter[5910]: level=info ts=2021-11-19T17:34:23.100Z caller=tls_config.go:191 msg="TLS is disabled." http2=false
  ```

1. Ознакомьтесь с опциями node_exporter и выводом `/metrics` по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.
Ответ:
 ```
node_network_receive_bytes_total{device="eth0"}  
node_network_receive_errs_total{device="eth0"}  
node_network_transmit_bytes_total{device="eth0"}  
node_network_transmit_errs_total{device="eth0"}

node_disk_io_time_seconds_total{device="sda"}
node_disk_read_bytes_total{device="sda"}  
node_disk_read_time_seconds_total{device="sda"}  
node_disk_written_bytes_total{device="sda"}
node_disk_write_time_seconds_total{device="sda"} 

node_memory_MemAvailable_bytes  
node_memory_MemFree_bytes  

node_cpu_seconds_total{cpu="0",mode="user"}
node_cpu_seconds_total{cpu="0",mode="idle"}  
node_cpu_seconds_total{cpu="0",mode="iowait"}  
node_cpu_seconds_total{cpu="0",mode="system"}  

node_cpu_seconds_total{cpu="1",mode="user"}
node_cpu_seconds_total{cpu="1",mode="idle"}  
node_cpu_seconds_total{cpu="1",mode="iowait"}  
node_cpu_seconds_total{cpu="1",mode="system"}  

process_cpu_seconds_total  


 ```
3. Установите в свою виртуальную машину [Netdata](https://github.com/netdata/netdata). Воспользуйтесь [готовыми пакетами](https://packagecloud.io/netdata/netdata/install) для установки (`sudo apt install -y netdata`). После успешной установки:
    * в конфигурационном файле `/etc/netdata/netdata.conf` в секции [web] замените значение с localhost на `bind to = 0.0.0.0`,
    * добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте `vagrant reload`:

    ```bash
    config.vm.network "forwarded_port", guest: 19999, host: 19999
    ```

    После успешной перезагрузки в браузере *на своем ПК* (не в виртуальной машине) вы должны суметь зайти на `localhost:19999`. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.
Ответ:

    На 0.0.0.0 повесить данный сервис в моем случае не получится в силу особенности конфигурации сетевых интерфейсов на машине. Повесил процесс на маршрутизируемый адрес
```

  
 root@vagrant:/home/vagrant# cat /etc/netdata/netdata.conf
[global]
        run as user = netdata
        web files owner = root
        web files group = root
        bind socket to IP = 172.28.128.3 
 ```
 ```
   vagrant@vagrant:~$ netstat -tulpan | grep 19999
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 172.28.128.3:19999      0.0.0.0:*               LISTEN    
```

Резултат:

![image](https://user-images.githubusercontent.com/44027303/142722120-1d3d5e8d-d290-457b-8fcd-1c3d92162d6d.png)


1. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?
Ответ:

Можно

```
root@vagrant:/home/vagrant# dmesg | grep -i virtual
[    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
[    0.002202] CPU MTRRs all blank - virtualized system.
[    0.088692] Booting paravirtualized kernel on KVM
[    2.323981] systemd[1]: Detected virtualization oracle.
```

3. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?
Ответ:
```
root@vagrant:/home/vagrant# cat /proc/sys/fs/nr_open
1048576
root@vagrant:/home/vagrant# /sbin/sysctl -n fs.nr_open
1048576
root@vagrant:/home/vagrant# 
```

nr_open - Максимальное число открытых дескрипторов файлов.

```
root@vagrant:/home/vagrant#  ulimit -n
1024
root@vagrant:/home/vagrant#  ulimit -Sn
1024
root@vagrant:/home/vagrant# /sbin/sysctl -n fs.nr_ope^C
root@vagrant:/home/vagrant#  ulimit -Hn
1048576
```

ulimit -n, ulimit -Sn - это мягкая версия лимитирования ресурсов

ulimit -Hn - это жесткая версия лимитирования ресурсов

5. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.
Ответ:

Терминал 1:
```
root@vagrant:/home/vagrant# sleep 1h &
[1] 8
root@vagrant:/home/vagrant# 
```

Терминал 2:
```
root@vagrant:/# ps aux | grep sleep
root           8  0.0  0.0   8076   528 pts/0    S    10:31   0:00 sleep 1h
root          19  0.0  0.0   8900   736 pts/1    S+   10:34   0:00 grep --color=auto sleep
root@vagrant:/# nsenter --target 8 --pid --mount    
root@vagrant:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3   9836  3976 pts/0    S+   10:31   0:00 /bin/bash
root           8  0.0  0.0   8076   528 pts/0    S    10:31   0:00 sleep 1h
root           9  0.0  0.4   9836  4204 pts/1    S    10:33   0:00 -bash
root          20  0.0  0.0   8996   696 pts/1    S    10:34   0:00 nsenter --target 8 --p
root          21  0.0  0.3   9836  4000 pts/1    S    10:34   0:00 -bash
root          30  0.0  0.3  11492  3388 pts/1    R+   10:34   0:00 ps aux
```


7. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?
Ответ:

В конце dmesdg после запуска видим:
```
[ 3353.491664] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-1.scope
```
systemd создаёт cgroup для каждого пользователя, все процессы пользователя принадлежат этой группе. Каждая c-группа имеет лимит.


Стандартное значение по умолчанию:
root@vagrant:/home/vagrant# sysctl kernel.threads-max
kernel.threads-max = 7142

Можно изменить число процессов TasksMax в /etc/systemd/system/user-.slice.d/15-limits.conf


```

```
 
 ---

## Как сдавать задания

Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в [Google Docs](https://docs.google.com/document/u/0/?tgif=d) и отправить в личном кабинете на проверку ссылку на ваш документ.
Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.1. Введение в DevOps — Сусанна Алиева".

Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка), иначе преподаватель не сможет проверить работу. Чтобы это проверить, откройте ссылку в браузере в режиме инкогнито.

[Как предоставить доступ к файлам и папкам на Google Диске](https://support.google.com/docs/answer/2494822?hl=ru&co=GENIE.Platform%3DDesktop)

[Как запустить chrome в режиме инкогнито ](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DDesktop&hl=ru)

[Как запустить  Safari в режиме инкогнито ](https://support.apple.com/ru-ru/guide/safari/ibrw1069/mac)

Любые вопросы по решению задач задавайте в чате Slack.

---
