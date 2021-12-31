#!/usr/bin/env python3

import os


bash_command = ["cd /home/dev_ops_learn/dev_ops_learn/", "git status"]
popen = os.popen(' && '.join(bash_command))
result_os = popen.read()
for result in result_os.split('\n'):
    if result.find('modified:') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        i = os.getcwd()
        print(i + '/' + prepare_result)
