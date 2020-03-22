import os
from os import path

files = os.listdir('out')

for fname in files:
    fname = path.join('out', fname)
    os.system('bdex upload "{}"'.format(fname))
    
