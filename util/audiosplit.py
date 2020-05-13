from os import path
import subprocess as subp
import argparse
import re

def fmt_tm(tm):
    return f'{tm//3600:02d}:{tm//60%60:02d}:{tm%60:02d}'

def split(fname, st, ed, ofname=None):
    if not ofname: ofname = fname
    subp.Popen(
        [
            'ffmpeg', '-i', fname, 
            '-ss', fmt_tm(st),
            '-to', fmt_tm(ed),
            '-acodec', 'copy', ofname,
        ],
        stdout=subp.PIPE,
        stderr=subp.PIPE,
    ).communicate()

def extname(fname):
    m = re.search(r'\.([^\.]+)$', fname)
    if not m: return ''
    else: return m.group(1)
    
def get_total(fname):
    res = subp.Popen(
        ['ffmpeg', '-i', fname],
        stdout=subp.PIPE,
        stderr=subp.PIPE,
    ).communicate()[1].decode('latin1')
    m = re.search(r'Duration: (\d+):(\d+):(\d+)', res)
    if not m: return None
    return [int(m.group(1)), int(m.group(2)), int(m.group(3))]
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', help='file name')
    parser.add_argument('--num', '-n', help='number to split', type=int, required=True)
    
    args = parser.parse_args()
    
    if not path.exists(args.fname):
        print('未找到文件')
        return
        
    ofname_temp = re.sub(r'\.[^\.]+$','', args.fname) + \
                  '-{st}-{ed}.mp3'
        
    total = get_total(args.fname)
    if not total:
        print('视频信息读取失败')
        return
    total = total[0] * 3600 + total[1] * 60 + total[2]
    
    each = total // args.num
    delims = [each * i for i in range(args.num)]
    delims.append(total)

    for st, ed in zip(delims[:-1], delims[1:]):
        ofname = ofname_temp.replace('{st}', str(st)) \
                 .replace('{ed}', str(ed))
        print(ofname)
        split(args.fname, st, ed, ofname)
    
if __name__ == '__main__': main()