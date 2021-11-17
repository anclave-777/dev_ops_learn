# Домашнее задание к занятию "3.3. Операционные системы, лекция 1"

1. Какой системный вызов делает команда `cd`? В прошлом ДЗ мы выяснили, что `cd` не является самостоятельной  программой, это `shell builtin`, поэтому запустить `strace` непосредственно на `cd` не получится. Тем не менее, вы можете запустить `strace` на `/bin/bash -c 'cd /tmp'`. В этом случае вы увидите полный список системных вызовов, которые делает сам `bash` при старте. Вам нужно найти тот единственный, который относится именно к `cd`.

Ответ:
```
vagrant@vagrant:~$ strace /bin/bash -c 'cd /tmp' 2>&1  | grep tmp
execve("/bin/bash", ["/bin/bash", "-c", "cd /tmp"], 0x7fff6e080ff0 /* 24 vars */) = 0
stat("/tmp", {st_mode=S_IFDIR|S_ISVTX|0777, st_size=4096, ...}) = 0
chdir("/tmp")                           = 0
vagrant@vagrant:~$ strace /bin/bash -c 'cd /tmp' 2>&1  | grep chdir
chdir("/tmp") - Ответ
```
2. Попробуйте использовать команду `file` на объекты разных типов на файловой системе. Например:
    ```bash
    vagrant@netology1:~$ file /dev/tty
    /dev/tty: character special (5/0)
    vagrant@netology1:~$ file /dev/sda
    /dev/sda: block special (8/0)
    vagrant@netology1:~$ file /bin/bash
    /bin/bash: ELF 64-bit LSB shared object, x86-64
    ```
    Используя `strace` выясните, где находится база данных `file` на основании которой она делает свои догадки.
 
 Ответ:
 ```
 База расположена  в /usr/share/misc/magic.mgc
 vagrant@vagrant:~$ strace -e trace=file /bin/bash -c 'file /dev/tty' 2>&1 | tail -10
stat("/home/vagrant/.magic.mgc", 0x7ffd0428cdd0) = -1 ENOENT (No such file or directory)
stat("/home/vagrant/.magic", 0x7ffd0428cdd0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)
stat("/etc/magic", {st_mode=S_IFREG|0644, st_size=111, ...}) = 0
openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY) = 3
lstat("/dev/tty", {st_mode=S_IFCHR|0666, st_rdev=makedev(0x5, 0), ...}) = 0
/dev/tty: character special (5/0)
+++ exited with 0 +++
```

3. Предположим, приложение пишет лог в текстовый файл. Этот файл оказался удален (deleted в lsof), однако возможности сигналом сказать приложению переоткрыть файлы или просто перезапустить приложение – нет. Так как приложение продолжает писать в удаленный файл, место на диске постепенно заканчивается. Основываясь на знаниях о перенаправлении потоков предложите способ обнуления открытого удаленного файла (чтобы освободить место на файловой системе).
  ` Ответ:  `
 
 

4. Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?
  ` Ответ: Нет, не занимает.  `
5. В iovisor BCC есть утилита `opensnoop`:
    ```bash
    root@vagrant:~# dpkg -L bpfcc-tools | grep sbin/opensnoop
    /usr/sbin/opensnoop-bpfcc
    ```
    На какие файлы вы увидели вызовы группы `open` за первую секунду работы утилиты? Воспользуйтесь пакетом `bpfcc-tools` для Ubuntu 20.04. Дополнительные [сведения по установке](https://github.com/iovisor/bcc/blob/master/INSTALL.md).


`Ответ: 
```
Ставим sudo apt-get install bpfcc-tools linux-headers-$(uname -r)


После выполняем команду
root@vagrant:/home/vagrant# dpkg -L bpfcc-tools | grep sbin/opensnoop   
/usr/sbin/opensnoop-bpfcc


Смотрим на результат:
root@vagrant:/home/vagrant# /usr/sbin/opensnoop-bpfcc
PID    COMM               FD ERR PATH
617    irqbalance          6   0 /proc/interrupts
617    irqbalance          6   0 /proc/stat
617    irqbalance          6   0 /proc/irq/20/smp_affinity
617    irqbalance          6   0 /proc/irq/0/smp_affinity
617    irqbalance          6   0 /proc/irq/1/smp_affinity
617    irqbalance          6   0 /proc/irq/8/smp_affinity
617    irqbalance          6   0 /proc/irq/12/smp_affinity
617    irqbalance          6   0 /proc/irq/14/smp_affinity
617    irqbalance          6   0 /proc/irq/15/smp_affinity
793    vminfo              4   0 /var/run/utmp
593    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
593    dbus-daemon        18   0 /usr/share/dbus-1/system-services
593    dbus-daemon        -1   2 /lib/dbus-1/system-services
593    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/
793    vminfo              4   0 /var/run/utmp
593    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
593    dbus-daemon        18   0 /usr/share/dbus-1/system-services
593    dbus-daemon        -1   2 /lib/dbus-1/system-services
593    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/
617    irqbalance          6   0 /proc/interrupts
617    irqbalance          6   0 /proc/stat
617    irqbalance          6   0 /proc/irq/20/smp_affinity
617    irqbalance          6   0 /proc/irq/0/smp_affinity
617    irqbalance          6   0 /proc/irq/1/smp_affinity
617    irqbalance          6   0 /proc/irq/8/smp_affinity
617    irqbalance          6   0 /proc/irq/12/smp_affinity
617    irqbalance          6   0 /proc/irq/14/smp_affinity
617    irqbalance          6   0 /proc/irq/15/smp_affinity
793    vminfo              4   0 /var/run/utmp
593    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
593    dbus-daemon        18   0 /usr/share/dbus-1/system-services
593    dbus-daemon        -1   2 /lib/dbus-1/system-services
593    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/
793    vminfo              4   0 /var/run/utmp
593    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
593    dbus-daemon        18   0 /usr/share/dbus-1/system-services
593    dbus-daemon        -1   2 /lib/dbus-1/system-services
593    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/
617    irqbalance          6   0 /proc/interrupts
617    irqbalance          6   0 /proc/stat
617    irqbalance          6   0 /proc/irq/20/smp_affinity
617    irqbalance          6   0 /proc/irq/0/smp_affinity
617    irqbalance          6   0 /proc/irq/1/smp_affinity
617    irqbalance          6   0 /proc/irq/8/smp_affinity 
```
`


1. Какой системный вызов использует `uname -a`? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в `/proc`, где можно узнать версию ядра и релиз ОС.
Ответ:
```
root@vagrant:/home/vagrant# strace uname -a
execve("/usr/bin/uname", ["uname", "-a"], 0x7ffe089a8888 /* 19 vars */) = 0
brk(NULL)                               = 0x556404508000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffd6f345c60) = -1 EINVAL (Invalid argument)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=24108, ...}) = 0
mmap(NULL, 24108, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f6b2bdaa000
```
Цитата:
```
Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osre‐ lease, version, domainname}.
```


3. Чем отличается последовательность команд через `;` и через `&&` в bash? Например:
    ```bash
    root@netology1:~# test -d /tmp/some_dir; echo Hi
    Hi
    root@netology1:~# test -d /tmp/some_dir && echo Hi
    root@netology1:~#
    ```
    Есть ли смысл использовать в bash `&&`, если применить `set -e`?
1. Из каких опций состоит режим bash `set -euxo pipefail` и почему его хорошо было бы использовать в сценариях?
1. Используя `-o stat` для `ps`, определите, какой наиболее часто встречающийся статус у процессов в системе. В `man ps` ознакомьтесь (`/PROCESS STATE CODES`) что значат дополнительные к основной заглавной буквы статуса процессов. Его можно не учитывать при расчете (считать S, Ss или Ssl равнозначными).

 
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
