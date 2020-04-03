import os
import sys
import re
from os import path


def check_lost():
    # check {dir} {list_file}
    
    li1 = os.listdir(sys.argv[1])

    co = open(sys.argv[2], encoding='utf-8').read()
    li2 = set(re.findall(r'^\| (.+?\.epub) .+? \|', co, re.M))
    #print(li2)

    li = [it for it in li1 if it not in li2]

    with open(sys.argv[2] + '.res.txt', 'w', encoding='utf-8') as f:
        for it in li: f.write(it + '\n')

def is_gbk(s):
    assert len(s) == 1
    try:
        s.encode('gbk')
        return True
    except:
        return False

def filter_fname(s):
    return ''.join([(ch if is_gbk(ch) else '-') for ch in s])


def batch_rename():
    # rename {dir}
    dir = sys.argv[1]
    files = os.listdir(dir)
    
    for f in files:
        nf = filter_fname(f)
        if f == nf: continue
        print(nf)
        f = path.join(dir, f)
        nf = path.join(dir, nf)
        os.rename(f, nf)

def upload():
    # upload {list_file} {dirname}
    dir = sys.argv[2]
    
    li = open(sys.argv[1], encoding='utf-8').read().split('\n')[:-1]
    
    for it in li:
        it = path.join(dir, it)
        os.system(f'bdex upload "{it}" | tee -a "log.txt"')
        
batch_rename()