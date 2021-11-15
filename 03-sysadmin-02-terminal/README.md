# Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"

1. Какого типа команда `cd`? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.
Ответ:
root@vagrant:/home/vagrant# type cd
cd is a shell builtin 

cd - встроенная команла shell оболочки, она меняет рабочую директорию процесса shell. Теоретически она могла бы быть отдельным приложением и менять cwd своего подпроцесса, но затем необходимо было передать это значение shell, что заняло бы дополнительные ресурсы. 


1. Какая альтернатива без pipe команде `grep <some_string> <some_file> | wc -l`? `man grep` поможет в ответе на этот вопрос. Ознакомьтесь с [документом](http://www.smallo.ruhr.de/award.html) о других подобных некорректных вариантах использования pipe.
Ответ:
grep <some_string> <some_file> -c



1. Какой процесс с PID `1` является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?
Ответ:
systemd.

root@vagrant:/home/vagrant# pstree -p | head -1
systemd(1)-+-VBoxService(793)-+-{VBoxService}(795)



1. Как будет выглядеть команда, которая перенаправит вывод stderr `ls` на другую сессию терминала?
Ответ:

У меня открыто 3 ssh сессии. При передаче команды с несуществующей директорией из 3 сессии

vagrant@vagrant:~$ ll /home2 2> /dev/pts/1

ошибка появилась в консоли терминала 2:
root@vagrant:/home/vagrant# ls: cannot access '/home2': No such file or directory


1. Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.
Ответ:
cat < /home/vagrant/test1.txt 1> /test2.txt

1. Получится ли вывести находясь в графическом режиме данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?
Ответ:
cat /home/vagrant/test1.txt >/dev/tty1


1. Выполните команду `bash 5>&1`. К чему она приведет? Что будет, если вы выполните `echo netology > /proc/$$/fd/5`? Почему так происходит?
Ответ:

root@vagrant:/home# bash 5>&1
root@vagrant:/home# echo netology > /proc/$$/fd/5
netology

bash 5>&1 - создаст новый файловый дескриптор 5 и перенаправит его на stdout (1) 
/proc/$$/fd - содержит ссылки для дескрипторов файлов, которые были открыты собственным процессом $$.

Из соседнего терминала команда не выполнится, без bash 5>&1:
root@vagrant:/home/vagrant# echo netology > /proc/$$/fd/5
bash: /proc/1031/fd/5: No such file or directory

1. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от `|` на stdin команды справа.
Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.
Ответ:
Получится
root@vagrant:/home#  ls /example 3>&2 2>&1 1>&3 | grep -n "file"
root@vagrant:/home#  1:ls: cannot access '/example': No such file or directory


1. Что выведет команда `cat /proc/$$/environ`? Как еще можно получить аналогичный по содержанию вывод?
Ответ:
vagrant@vagrant:~$ cat /proc/$$/environ
USER=vagrantLOGNAME=vagrantHOME=/home/vagrantPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/binSHELL=/bin/bashTERM=xtermXDG_SESSION_ID=32XDG_RUNTIME_DIR=/run/user/1000DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/busXDG_SESSION_TYPE=ttyXDG_SESSION_CLASS=userMOTD_SHOWN=pamLANG=en_US.UTF-8LANGUAGE=en_US:SSH_CLIENT=172.28.128.1 53235 22SSH_CONNECTION=172.28.128.1 53235 172.28.128.3 22SSH_TTY=/dev/pts/1vagrant@vagrant:~$ 

Аналог - env


1. Используя `man`, опишите что доступно по адресам `/proc/<PID>/cmdline`, `/proc/<PID>/exe`.
Ответ:
man proc | grep -C 10 cmdline

/proc/[pid]/cmdline - файл, доступный только для чтения. Содержит полную командную строку и аргументы, в которой запущен данный процесс

man proc | grep -C 5 exe

/proc/[pid]/exe - символьная ссылка на файл, который запускал процесс

1. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью `/proc/cpuinfo`.
Ответ:
SSE4_2
vagrant@vagrant:~$ cat /proc/cpuinfo | grep sse
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single fsgsbase avx2 invpcid rdseed clflushopt md_clear flush_l1d arch_capabilities
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single fsgsbase avx2 invpcid rdseed clflushopt md_clear flush_l1d arch_capabilities

1. При открытии нового окна терминала и `vagrant ssh` создается новая сессия и выделяется pty. Это можно подтвердить командой `tty`, которая упоминалась в лекции 3.2. Однако:

    ```bash
	vagrant@netology1:~$ ssh localhost 'tty'
	not a tty
    ```

	Почитайте, почему так происходит, и как изменить поведение.
Ответ:
tty выводит имя терминала, связанного с stdin. Нужно добавть в команду ключ:

     -t      Force pseudo-terminal allocation.  This can be used to execute arbitrary
             screen-based programs on a remote machine, which can be very useful, e.g.
             when implementing menu services.  Multiple -t options force tty alloca‐
             tion, even if ssh has no local tty.

Часть вывода команды man ssh 
В результате:
vagrant@vagrant:~$ ssh localhost 'tty' -t
The authenticity of host 'localhost (::1)' can't be established.
ECDSA key fingerprint is SHA256:wSHl+h4vAtTT7mbkj2lbGyxWXWTUf6VUliwpncjwLPM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? ^C


1. Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись `reptyr`. Например, так можно перенести в `screen` процесс, который вы запустили по ошибке в обычной SSH-сессии.
Ответ:
Устанавливаем reptur
vim test - открываем файл в 1 терминале
vagrant@vagrant:~$ vim test

Идем во второй и устанавливаем значение kernel.yama.ptrace_scope = 0
vagrant@vagrant:~$ sudo vim /etc/sysctl.d/10-ptrace.conf

Применяем параметры ядра
vagrant@vagrant:~$ sysctl -p /etc/sysctl.d/10-ptrace.conf
sysctl: permission denied on key "kernel.yama.ptrace_scope", ignoring
vagrant@vagrant:~$ sudo sysctl -p /etc/sysctl.d/10-ptrace.conf
kernel.yama.ptrace_scope = 0

Выясняем pid  терминале
vagrant@vagrant:~$ ps -ef | grep test
vagrant     2682    2231  0 18:03 pts/1    00:00:00 vim test

и открываем его
reptyr -s 2682

1. `sudo echo string > /root/new_file` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без `sudo` под вашим пользователем. Для решения данной проблемы можно использовать конструкцию `echo string | sudo tee /root/new_file`. Узнайте что делает команда `tee` и почему в отличие от `sudo echo` команда с `sudo tee` будет работать.
Ответ:
Посмотреть описание рабоыт можно в man
Команда tee читает из stdin и пишет в stdout и файлы

В sudo echo string - sudo применяется к echo, а не к записи в файл.

sudo tee - sudo применяется к tee, таким образом у tee будут права на запись в файл. Таким образом echo выполняется без sudo (обычным пользователем), а вывод stdout echo перенаправляется на stdin tee, запущенной от sudo, и она записывает данные в файл.

 
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
