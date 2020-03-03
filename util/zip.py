import os
import sys
from os import path
import subprocess as subp

max_sz = 100 * 1024 * 1024

def main():
    dir = sys.argv[1]
    files = map(lambda f: path.join(dir, f), os.listdir(dir))
    files = list(filter(lambda f: path.getsize(f) <= max_sz, files))
    
    zips = []
    start = 0
    total = 0
    
    for i, f in enumerate(files):
        sz = path.getsize(f)
        if total + sz > max_sz:
            zips.append(files[start:i])
            start = i
            total = sz
        else:
            total += sz
    zips.append(files[start:])
    print(len(zips))
    
    for i, z in enumerate(zips):
        subp.Popen(['7z', 'a', '-mx0', path.join(dir, f'{i}.7z'), *z])

if __name__ == '__main__': main()
