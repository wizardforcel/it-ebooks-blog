var process = require('child_process');

var getTimeStr = function() {
    
    var tm = new Date();
    var o = {
        yr: tm.getFullYear(),
        mon: tm.getMonth() + 1,
        dt: tm.getDate(),
        hr: tm.getHours(),
        min: tm.getMinutes(),
        sec: tm.getSeconds()
    };
    for(var i in o)
    {
        o[i] = o[i].toString();
        if(o[i].length < 2)
            o[i] = '0' + o[i];
    }
    return o.yr + '-' + o.mon + '-' + o.dt + 
        ' ' + o.hr + ':' + o.min + ':' + o.sec;
};

var cmds = [
    'git add -A',
    'git commit -m "' + getTimeStr() + '"',
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
