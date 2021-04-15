var fs = require('fs')
var request = require('sync-request')
var cheerio = require('cheerio')

var repoList = process.argv[2].split(':')

var urlTemp = 'https://gitee.com/it-ebooks/{repo}'

var coTemp = `
## {title}

+   [Gitee 下载](https://gitee.com/it-ebooks/{repo}/raw/master/{fname})
+   [Github 下载](https://cdn.jsdelivr.net/gh/it-ebooks-0/{repo}/{fname})
+   [Gitlab 下载](https://gitlab.com/it-ebooks/{repo}/raw/master/{fname})
`

var ofile = fs.openSync('out.md', 'w')

for(var repo of repoList) {
    
    var url = urlTemp.replace('{repo}', repo)
    console.log(url)
    var html = request('GET', url, {timeout: 20000}).getBody().toString()
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
    var $list = $('div.five.column a')
    var res = []
    for(var i = 0; i < $list.length; i++) {
        res.push($list.eq(i).text())
    }
    return res.filter(x => x != 'README.md')
}
