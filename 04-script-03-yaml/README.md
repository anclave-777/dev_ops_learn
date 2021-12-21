# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
	```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
	```
  Нужно найти и исправить все ошибки, которые допускает наш сервис
  
  
  
  Ответ:
  
  Правильный json
  
  ```
  {
  "info": "Sample JSON output from our service \\t",
  "elements": [
    {
      "name": "first",
      "type": "server",
      "ip": "71.75.22.43"
    },
    {
      "name": "second",
      "type": "proxy",
      "ip": "71.78.22.43"
    }
  ]
}
```


## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3
  
import socket
from datetime import datetime
from os import path
import time
import json
import yaml


site = {
"drive.google.com": "",
"mail.google.com": "",
"google.com": ""
}


def write_json():
    with open('site.yaml', 'w') as yaml_file:
        yaml.dump(site, yaml_file, default_flow_style=False)
    with open('site.json', 'w') as json_file:
        json.dump(site, json_file, indent=2)


while (True):
    for sites, known_ip in site.items():
        try:
            new_ip = socket.gethostbyname(sites)
           #print(new_ip)
            if (not path.exists('site.yaml') or not path.exists('site.json')):
                write_json()
            if (known_ip != "" and known_ip != new_ip):
                print(f'[ERROR] {sites} IP mismatch: {known_ip} {new_ip}')
                write_json()
            else:
                print(f'{sites} - {new_ip}')
            site[sites] = new_ip
        except:
            print('Something goes wrong')
    time.sleep(5)
```

### Вывод скрипта при запуске при тестировании:
```
vagrant@vagrant:~$ ./yumljson.py  
drive.google.com - 64.233.163.194
mail.google.com - 74.125.131.17
google.com - 64.233.161.100
drive.google.com - 64.233.163.194
mail.google.com - 74.125.131.17
[ERROR] google.com IP mismatch: 64.233.161.100 64.233.161.113
drive.google.com - 64.233.163.194
mail.google.com - 74.125.131.17
[ERROR] google.com IP mismatch: 64.233.161.113 74.125.131.139
drive.google.com - 64.233.163.194
mail.google.com - 74.125.131.17
[ERROR] google.com IP mismatch: 74.125.131.139 74.125.131.100
drive.google.com - 64.233.163.194
mail.google.com - 74.125.131.17
google.com - 74.125.131.100
drive.google.com - 64.233.163.194
mail.google.com - 74.125.131.17
google.com - 74.125.131.100
drive.google.com - 64.233.163.194
[ERROR] mail.google.com IP mismatch: 74.125.131.17 173.194.73.18
google.com - 74.125.131.100
drive.google.com - 64.233.163.194
[ERROR] mail.google.com IP mismatch: 173.194.73.18 173.194.73.17
google.com - 74.125.131.100
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
vagrant@vagrant:~$ cat site.json 
{
  "drive.google.com": "64.233.163.194",
  "mail.google.com": "74.125.131.17",
  "google.com": "74.125.131.139"
  }
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
vagrant@vagrant:~$ cat site.yaml 
drive.google.com: 64.233.163.194
google.com: 74.125.131.100
mail.google.com: 74.125.131.17
```
    


## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

---

### Как сдавать задания

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
