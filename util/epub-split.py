import os
import sys
from os import path
import re
import time

dir = sys.argv[1]
st = int(sys.argv[2])
ed = int(sys.argv[3])

textdir = path.join(dir, 'OEBPS', 'Text')
imgdir = path.join(dir, 'OEBPS', 'Images')

subfix = str(int(time.time() * 1000))
os.mkdir(textdir + subfix)
os.mkdir(imgdir + subfix)

imgs = []

for i in range(st, ed + 1):
    try:
        f = path.join(textdir, f'{i}.html')
        print(f)
        co = open(f, encoding='utf8').read()
        imgs_ = re.findall(r'Images/(\w+\.jpg)', co)
        imgs += imgs_
        nf = path.join(textdir + subfix, f'{i}.html')
        os.rename(f, nf)
    except Exception as ex:
        print(ex)
    
for img in imgs:
    f = path.join(imgdir, img)
    print(f)
    nf = path.join(imgdir + subfix, img)
    try: os.rename(f, nf)
    except: pass
    
logfile = path.join(dir, 'OEBPS', 'imgs' + subfix + '.txt')

with open(logfile, 'w', encoding='utf8') as f:
    for img in imgs: f.write(f'<item href="Images/{img}" id="{img}" media-type="image/jpeg"/>\n')