# Самоконтроль выполненения задания

1. Где расположен файл с `some_fact` из второго пункта задания?
group_vars/all/examp.yml 
3. Какая команда нужна для запуска вашего `playbook` на окружении `test.yml`?
ansible-playbook -i inventory/test.yml site.yml 
5. Какой командой можно зашифровать файл?
ansible-vault encrypt group_vars/deb/examp.yml 
7. Какой командой можно расшифровать файл?
ansible-vault decrypt group_vars/deb/examp.yml 
9. Можно ли посмотреть содержимое зашифрованного файла без команды расшифровки файла? Если можно, то как?
ansible-vault edit  group_vars/deb/examp.yml 
11. Как выглядит команда запуска `playbook`, если переменные зашифрованы?
ansible-playbook --ask-vault-pass playbook.yml
13. Как называется модуль подключения к host на windows?
winrm
15. Приведите полный текст команды для поиска информации в документации ansible для модуля подключений ssh
ansible-doc -t connection ssh
17. Какой параметр из модуля подключения `ssh` необходим для того, чтобы определить пользователя, под которым необходимо совершать подключение?
remote_user
