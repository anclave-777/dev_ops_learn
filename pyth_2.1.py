#!/usr/bin/env python3

import os
import sys


i = os.getcwd()

if len(sys.argv) >= 2: 
    i = sys.argv[1]

bash_command = [ f"cd {i}", "cd /home/dev_ops_learn/dev_ops_learn/", "git status"]
popen = os.popen(' && '.join(bash_command))
result = popen.read()
popen.close()
for res in result.split('\n'):
    if res.find('modified:') != -1:
        prepare_result = res.replace('\tmodified:   ', '')
        print(f'{os.path.join(os.getcwd(), prepare_result)}')
