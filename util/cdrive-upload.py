import os
import sys
from os import path
import subprocess as subp

drivers = ['baijia', 'csdn', 'jian', 'sohu', 'weibo']

dir = sys.argv[1]
files = os.listdir(dir)

for d in drivers:
    for f in files:
        print(f)
        f = path.join(dir, f)
        os.system(f'cdrive upload {d} "{f}" | tee -a log.txt')