# Домашнее задание к занятию «2.4. Инструменты Git»

Для выполнения заданий в этом разделе давайте склонируем репозиторий с исходным кодом 
терраформа https://github.com/hashicorp/terraform +Выполнено

В виде результата напишите текстом ответы на вопросы и каким образом эти ответы были получены. 

1. Найдите полный хеш и комментарий коммита, хеш которого начинается на `aefea`.

----
Ответ:
root@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git show aefea --pretty=oneline
aefead2207ef7e2aa5dc81a34aedf0cad4c32545(Полный хеш) Update CHANGELOG.md(комментарий)

1. Какому тегу соответствует коммит `85024d3`?

----
Ответ:
root@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git tag --points-at 85024d3
v0.12.23

1. Сколько родителей у коммита `b8d720`? Напишите их хеши.

----
Ответ:
2 коммита, хеши смотрел командой:
root@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git cat-file -p b8d720f | grep parent                           
parent 56cd7859e05c36c06b56d013b55a252d0bb7e158
parent 9ea88f22fc6269854151c571162c5bcf958bee2


1. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами  v0.12.23 и v0.12.24.

----
Ответ:
root@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git log --pretty=format:"%H %B" v0.12.23..v0.12.24
33ff1c03bb960b332be3af2e333462dde88b279e v0.12.24

b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links

3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md

6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable

Non-HTTP errors previously resulted in a panic due to dereferencing the
resp pointer while it was nil, as part of rendering the error message.
This commit changes the error message formatting to cope with a nil
response, and extends test coverage.

Fixes #24384

5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location

Since these links were in the soon-to-be-deprecated 0.11 language section, I
think we can just remove them without needing to find an equivalent link.

06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows

4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release


1. Найдите коммит в котором была создана функция `func providerSource`, ее определение в коде выглядит 
так `func providerSource(...)` (вместо троеточего перечислены аргументы).

----
Ответ:
t@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git log -S "func providerSource"  --reverse --pretty=format:"%H, %an, %ad, %s" |  head -n 1 
8c928e83589d90a031f811fae52a81be7153e82f, Martin Atkins, Thu Apr 2 18:04:39 2020 -0700, main: Consult local directories as potential mirrors of providers

1. Найдите все коммиты в которых была изменена функция `globalPluginDirs`.


----
Ответ:
root@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git log -S "globalPluginDirs"
commit 35a058fb3ddfae9cfee0b3893822c9a95b920f4c
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Oct 19 17:40:20 2017 -0700

    main: configure credentials from the CLI config file

commit c0b17610965450a89598da491ce9b6b5cbd6393f
Author: James Bardin <j.bardin@gmail.com>
Date:   Mon Jun 12 15:04:40 2017 -0400

    prevent log output during init
    
    The extra output shouldn't be seen by the user, and is causing TFE to
    fail.

commit 8364383c359a6b738a436d1b7745ccdce178df47
Author: Martin Atkins <mart@degeneration.co.uk>
Date:   Thu Apr 13 18:05:58 2017 -0700

    Push plugin discovery down into command package
    
    Previously we did plugin discovery in the main package, but as we move
    towards versioned plugins we need more information available in order to
    resolve plugins, so we move this responsibility into the command package
    itself.
    
    For the moment this is just preserving the existing behavior as long as
    there are only internal and unversioned plugins present. This is the
    final state for provisioners in 0.10, since we don't want to support
    versioned provisioners yet. For providers this is just a checkpoint along
    the way, since further work is required to apply version constraints from
    configuration and support additional plugin search directories.
    
    The automatic plugin discovery behavior is not desirable for tests because
    we want to mock the plugins there, so we add a new backdoor for the tests
    to use to skip the plugin discovery and just provide their own mock
    implementations. Most of this diff is thus noisy rework of the tests to
    use this new mechanism.

1. Кто автор функции `synchronizedWriters`? 


----
Ответ:
root@vagrant:/home/dev_ops_learn/dev_ops_learn/02-git-04-tools/terraform# git log -S "synchronizedWriters"
commit bdfea50cc85161dea41be0fe3381fd98731ff786
Author: James Bardin <j.bardin@gmail.com>
Date:   Mon Nov 30 18:02:04 2020 -0500

    remove unused

commit fd4f7eb0b935e5a838810564fd549afe710ae19a
Author: James Bardin <j.bardin@gmail.com>
Date:   Wed Oct 21 13:06:23 2020 -0400

    remove prefixed io
    
    The main process is now handling what output to print, so it doesn't do
    any good to try and run it through prefixedio, which is only adding
    extra coordination to echo the same data.

commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5
Author: Martin Atkins <mart@degeneration.co.uk>   -- Автор функции
Date:   Wed May 3 16:25:41 2017 -0700

    main: synchronize writes to VT100-faker on Windows
    
    We use a third-party library "colorable" to translate VT100 color
    sequences into Windows console attribute-setting calls when Terraform is
    running on Windows.
    
    colorable is not concurrency-safe for multiple writes to the same console,
    because it writes to the console one character at a time and so two
    concurrent writers get their characters interleaved, creating unreadable
    garble.
    
    Here we wrap around it a synchronization mechanism to ensure that there
    can be only one Write call outstanding across both stderr and stdout,
    mimicking the usual behavior we expect (when stderr/stdout are a normal
    file handle) of each Write being completed atomically.

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
