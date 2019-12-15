var fs = require('fs')
var request = require('sync-request')
var cheerio = require('cheerio')

var repoList = [
    'it-ebooks-2017-01to02',
    'it-ebooks-201703-part1',
    'it-ebooks-201703-part2',
    'it-ebooks-201703-part3',
    'it-ebooks-2017-04to06',
    'it-ebooks-2017-07to11',
    'it-ebooks-201712',
]

var urlTemp = 'https://github.com/it-ebooks/{repo}'

var coTemp = `
## {title}

+   [Gitee 下载](https://gitee.com/it-ebooks/{repo}/raw/master/{fname})
+   [Github 下载](https://github.com/it-ebooks/{repo}/raw/master/{fname})
+   [SourceForge 下载](https://sourceforge.net/p/{repo}/code/ci/master/tree/{fname}?format=raw)
`

var ofile = fs.openSync('out.md', 'w')

for(var repo of repoList) {
    
    var url = urlTemp.replace('{repo}', repo)
    console.log(url)
    var html = request('GET', url).getBody().toString()
    var flist = getFileList(html)
    
    for(var fname of flist) {
        
        var title = fname.replace(/\.\w+$/, '')
        var fname = encodeURIComponent(fname)
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
        
        var co = coTemp
            .replace(/\{title\}/g, title)
            .replace(/\{repo\}/g, repo)
            .replace(/\{fname\}/g, fname)
            
        fs.writeSync(ofile, co)
    }
    
}

fs.closeSync(ofile)
console.log('done..')

function getFileList(html) {
    
    var $ = cheerio.load(html)
    var $list = $('.content a')
    var res = []
    for(var i = 0; i < $list.length; i++) {
        res.push($list.eq(i).text())
    }
    return res.filter(x => x != 'README.md')
}
