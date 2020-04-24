var process = require('child_process');
var moment = require('moment')

var tmstr = moment().format('YYYY-MM-DD HH:mm:ss')
var cmds = [
    'git add -A',
    'git commit -m "' + tmstr + '"',
    'git push',
    'hexo clean',
    'hexo g -d'
];

for(var cmd of cmds) {
    try {
        console.log(cmd);
        console.log(process.execSync(cmd).toString());
    } catch(ex) {
        console.log(ex.toString());
    }
}
