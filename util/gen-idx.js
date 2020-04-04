var fs = require('fs')

var RE_LI = new RegExp(
    "^##\\x20+(.+?)\\s+" +
    "\\+   \\[Gitee 下载\\]\\((.+?)\\)\\s+" +
    "\\+   \\[Github 下载\\]\\((.+?)\\)\\s+" +
    "\\+   \\[SourceForge 下载\\]\\((.+?)\\)",
    "mg"
)
var RE_TR = /^\| (.+?) \(.+?\) \| (.+?) \|$/mg

function parseContent(idcs, md) {
    
    var m
    while(m = RE_LI.exec(md)) {
        var title = m[1],
            gitee = m[2],
            github = m[3],
            sourceforge = m[4]
        
        idcs[title] = idcs[title] || {}
        idcs[title].gitee = gitee
        idcs[title].github = github
        idcs[title].sourceforge = sourceforge
    }
    
    while(m = RE_TR.exec(md)) {
        var title = m[1],
            link = m[2]
        var prefix = link.split('://')[0]
        
        idcs[title] = idcs[title] || {}
        idcs[title][prefix] = link
    }
}

function main() {
    
    var fname = process.argv[2]
    if(!fname.endsWith('.md')) {
        console.log('请提供 MD 文件')
    }

    var res = {}
    var md = fs.readFileSync(fname)
    parseContent(res, md)
    
    fs.writeFileSync(
        fname + '.json', 
        JSON.stringify(res)
    )
}

if(require.main === module) main()