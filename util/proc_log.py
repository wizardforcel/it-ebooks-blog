# coding: utf-8

import sys
import re
from os import path

RE_LINK = r'^\[.+?\] (.+?) 上传完毕, .+?\n\[.+?\] META URL -> (.+?)$'

f = sys.argv[1]
co = open(f, encoding='utf-8').read()
links = re.findall(RE_LINK, co, re.M)
# links = {k:v for k, v in links}
print(f'count: {len(links)}')
res = [f'| {n} | {l} |' for n, l in links]
res = '| 文档 | 链接 |\n| --- | --- |\n' + '\n'.join(res)
outf = open(f + '.md', 'w', encoding='utf-8')
outf.write(res)
outf.close()
