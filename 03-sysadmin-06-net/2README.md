Работа c HTTP через телнет.


1. Подключитесь утилитой телнет к сайту stackoverflow.com telnet stackoverflow.com 80
отправьте HTTP 

```
GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]
```

В ответе укажите полученный HTTP код, что он означает?

Ответ:
```
vagrant@vagrant:~$ telnet stackoverflow.com 80
Trying 151.101.193.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com

HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: abe9acc1-6a61-4aba-aab1-7dd5a39c5400
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Fri, 26 Nov 2021 12:04:56 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-fra19120-FRA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1637928296.004878,VS0,VE93
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=e217b74b-99f9-980a-8fe9-4f5e873509d1; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly

Connection closed by foreign host.
```


Код перенаправления "301 Moved Permanently" протокола передачи гипертекста (HTTP) показывает, что запрошенный ресурс был окончательно перемещён в URL, указанный в заголовке https://stackoverflow.com/questions


2. Повторите задание 1 в браузере, используя консоль разработчика F12.
откройте вкладку Network
отправьте запрос http://stackoverflow.com
найдите первый ответ HTTP сервера, откройте вкладку Headers
укажите в ответе полученный HTTP код.
проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?
приложите скриншот консоли браузера в ответ.



Ответ:
![image](https://user-images.githubusercontent.com/44027303/143583484-2d09ad1a-100c-4f1e-8633-dca0e5e02ecc.png)






3 Какой IP адрес у вас в интернете?

Ответ
```
vagrant@vagrant:~$ curl https://ifconfig.me/
5.144.123.65vagrant@vagrant:~$ 
```

4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois

Ответ:

```
vagrant@vagrant:~$ whois 5.144.123.65        
% This is the RIPE Database query service.
% The objects are in RPSL format.
%
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf

% Note: this output has been filtered.
%       To receive output for a database update, use the "-B" flag.

% Information related to '5.144.96.0 - 5.144.127.255'

% Abuse contact for '5.144.96.0 - 5.144.127.255' is 'abuse@mtu.ru'

inetnum:        5.144.96.0 - 5.144.127.255
netname:        RU-MTU-20120711
country:        RU
org:            ORG-ZM1-RIPE
admin-c:        LTr1-RIPE
tech-c:         LTr1-RIPE
status:         ALLOCATED PA
remarks:        -----------------------------------------------
remarks:        ******* Spam, Viruses: abuse@mtu.ru *******
remarks:        ****** Site: http://spb.lancktelecom.ru/ ******
remarks:        ***********************************************
mnt-by:         RIPE-NCC-HM-MNT
mnt-by:         MTU-NOC
mnt-routes:     MTU-NOC
mnt-lower:      LANCK-MNT
mnt-lower:      MTU-NOC
mnt-routes:     LANCK-MNT
created:        2012-07-11T11:01:35Z
last-modified:  2018-08-22T09:48:57Z
source:         RIPE # Filtered

organisation:   ORG-ZM1-RIPE
org-name:       MTS PJSC
country:        RU
org-type:       LIR
address:        Petrovsky blvd 12, bldg 3
address:        127051
address:        Moscow
address:        RUSSIAN FEDERATION
phone:          +74957213499
fax-no:         +74992318129
admin-c:        LAP-RIPE
admin-c:        SAAP-RIPE
admin-c:        TABY-RIPE
admin-c:        LMUR-RIPE
admin-c:        YUF-RIPE
admin-c:        RPS-RIPE
abuse-c:        MAB8359-RIPE
mnt-ref:        RIPE-NCC-HM-MNT
mnt-ref:        MTU-NOC
mnt-by:         RIPE-NCC-HM-MNT
mnt-by:         MTU-NOC
created:        2004-04-17T11:55:44Z
last-modified:  2021-10-28T18:07:36Z
source:         RIPE # Filtered

role:           Mobile TeleSystems NW role
address:        PJSC "Mobile TeleSystems"
address:        Malay Monetnaya d.2a
address:        197101, Saint Petersburg
address:        Russia
phone:          +7 812 318 1211
fax-no:         +7 812 333 3131
remarks:        ---------------------------------------------------
remarks:        ***************************************************
remarks:        ********* Spam, Viruses: abuse@mtu.ru *********
remarks:        ***************************************************
remarks:        ---------------------------------------------------
abuse-mailbox:  abuse@mtu.ru
admin-c:        MTU1-RIPE
tech-c:         MTU1-RIPE
nic-hdl:        LTr1-RIPE
mnt-by:         LANCK-MNT
created:        2004-08-18T07:16:13Z
last-modified:  2020-12-17T10:04:08Z
source:         RIPE # Filtered

% Information related to '5.144.96.0/19AS8359'

route:          5.144.96.0/19
descr:          Mobile TeleSystems PJSC, Saint-Petersburg division
origin:         AS8359
mnt-by:         LANCK-MNT
mnt-by:         MTU-NOC
created:        2016-06-04T18:47:54Z
last-modified:  2016-06-04T18:47:54Z
source:         RIPE

% This query was served by the RIPE Database Query Service version 1.101 (WAGYU)
```

Провайдер descr:          Mobile TeleSystems PJSC, Saint-Petersburg division, Автономка  AS8359


Правильнее смотреть свой адрес в базах  RIPE или причатных. whois не всегда точно покажет принадлежность и контакты.


5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute

```
C:\Users\volan>tracert -d 8.8.8.8

Трассировка маршрута к 8.8.8.8 с максимальным числом прыжков 30

  1     1 ms     1 ms     1 ms  192.168.0.1
  2     *        *        *     Превышен интервал ожидания для запроса.
  3     4 ms     4 ms     5 ms  176.241.100.161
  4     3 ms     2 ms     3 ms  212.188.28.146
  5     4 ms     2 ms     4 ms  74.125.49.108
  6     6 ms     3 ms     7 ms  74.125.244.129
  7     3 ms     2 ms     5 ms  74.125.244.132
  8    10 ms    18 ms     6 ms  142.251.61.219
  9    10 ms    24 ms    10 ms  172.253.51.239
 10
 ```
 
 
 AS8359 -> гугловые AS -> AS15169
 
6. Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?


 ```                                                                                                                                      Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. _gateway                                                                                                                                    0.0%    64    0.1   0.2   0.1   0.5   0.1
 2. 192.168.0.1                                                                                                                                 1.6%    64    6.4  12.6   1.1 177.8  24.6
 3. (waiting for reply)
 4. 176.241.100.161                                                                                                                             0.0%    63   27.1  22.2   3.6 348.7  49.4
 5. bor-cr02-ae2.78.spb.mts-internet.net                                                                                                        0.0%    63    7.0  18.6   2.6 297.9  43.7
 6. 74.125.49.108                                                                                                                               0.0%    63   12.9  14.1   2.6 248.7  34.0
 7. 74.125.244.129                                                                                                                              1.6%    63    6.3  14.4   3.4 214.5  30.2
 8. 74.125.244.132                                                                                                                              0.0%    63    7.0  17.6   2.9 163.1  27.6
 9. 142.251.61.219                                                                                                                              0.0%    63   45.7  19.0   6.5 116.4  20.9
10. 172.253.51.239                                                                                                                              1.6%    63   11.1  15.3   8.0  66.8  10.5
11. (waiting for reply)
12. (waiting for reply)
13. (waiting for reply)
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. (waiting for reply)
18. (waiting for reply)
19. (waiting for reply)
20. dns.google                                                                                                                                  1.6%    63   47.1  23.3   6.1 387.5  50.6
 ```
 
На 4 хопе.



Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig

Ответ:


 ```
vagrant@vagrant:~$ dig dns.google

; <<>> DiG 9.16.1-Ubuntu <<>> dns.google
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 22061
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;dns.google.                    IN      A

;; ANSWER SECTION:
dns.google.             770     IN      A       8.8.8.8
dns.google.             770     IN      A       8.8.4.4

;; Query time: 23 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fri Nov 26 17:57:46 UTC 2021
;; MSG SIZE  rcvd: 71
```

Отвечает сервер на виртуальной машине:
;; SERVER: 127.0.0.53#53(127.0.0.53)


А записи
dns.google.             770     IN      A       8.8.8.8
dns.google.             770     IN      A       8.8.4.4




8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig

Ответ:

```
vagrant@vagrant:~$ dig  -x 8.8.8.8

; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6408
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;8.8.8.8.in-addr.arpa.          IN      PTR

;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.   6762    IN      PTR     dns.google.

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fri Nov 26 18:02:22 UTC 2021
;; MSG SIZE  rcvd: 73

vagrant@vagrant:~$ dig  -x 8.8.4.4

; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.4.4
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12457
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;4.4.8.8.in-addr.arpa.          IN      PTR

;; ANSWER SECTION:
4.4.8.8.in-addr.arpa.   11163   IN      PTR     dns.google.

;; Query time: 51 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fri Nov 26 18:03:17 UTC 2021
;; MSG SIZE  rcvd: 73
```

В качестве ответов на вопросы можно приложите лог выполнения команд в консоли или скриншот полученных результатов.

Как сдавать задания
Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в Google Docs и отправить в личном кабинете на проверку ссылку на ваш документ. Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.1. Введение в DevOps — Сусанна Алиева".

Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка), иначе преподаватель не сможет проверить работу. Чтобы это проверить, откройте ссылку в браузере в режиме инкогнито.

Как предоставить доступ к файлам и папкам на Google Диске

Как запустить chrome в режиме инкогнито

Как запустить Safari в режиме инкогнито

Любые вопросы по решению задач задавайте в чате Slack.

