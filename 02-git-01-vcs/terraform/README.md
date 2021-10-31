
# Local .terraform directories # - знак комментария, им помечаются строки в конфиге, которые не используются
**/.terraform/* - звездочка это символ обозначающий любое значение в рамках шаблона игнорируемого gitignore. В данном случае исключается локальная директория терраформа

# .tfstate files - Не обрабатывать файлы со статусом
*.tfstate
*.tfstate.*

# Crash log files 
crash.log - исключаются файлы с логами падений.

# Exclude all .tfvars files, which are likely to contain sentitive data, such as
# password, private keys, and other secrets. These should not be part of version
# control as they are data points which are potentially sensitive and subject
# to change depending on the environment.
#
*.tfvars - Тут описывается, что файлы с расширением  tfvars, в которых содержаться пароли, ключи и прочее будут исключены из обработки git

# Ignore override files as they are usually used to override resources locally and so
# are not checked in - Игнорируется еще 4 типа файлов
override.tf
override.tf.json
*_override.tf
*_override.tf.json

2 секции ниже закоменчены

# Include override files you do wish to add to version control using negated pattern
#
# !example_override.tf

# Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan
# example: *tfplan*


Игнорируются файлы настройки командой строки под терраформ.
# Ignore CLI configuration files
.terraformrc
terraform.rc
