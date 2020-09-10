import os
import re
import datetime

script_path = os.getcwd()
abs_path = script_path
file_pathes = os.listdir(abs_path)
print(file_pathes)
for file_path in file_pathes:
    if file_path == '.DS_Store' or file_path == 'update_ksn.py':
        continue
    q_num = os.path.basename(file_path)
    file_path = os.path.join(abs_path, file_path, "write_up.md")
    filename = os.path.basename(file_path)
    print(file_path)
    if not os.path.exists(file_path) or not filename == 'write_up.md':
        continue

    text = ""
    date = datetime.datetime.fromtimestamp(os.stat(file_path).st_birthtime)
    with open(file_path, 'r') as file:
        text = file.read()

    head = """
---
title: ksnctf Q.{0}
date: '{1}'
draft: false
category: 'CTF'
tags:
    - 'ksnctf'
cover: '../media/'
---
            """.format(q_num, date.strftime('%Y-%m-%d'))

    with open(file_path, 'w') as file:
        file.write(head + text)


