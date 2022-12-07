// Read File ../input.txt

// Part 1 


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    let f = {}, r = []; text.split('\n').forEach((l, i)=>{
        if(m=l.match(/cd (.+)/)){
            if(m[1] == '..') r.pop();
            else r.push(m[1] + '/');
        }
        if(m=l.match(/\d+/)){
            for (let i = r.length; i > 0; i--) {
                let d = r.slice(0, i).join('');
                (f[d]) ? f[d] += parseInt(m[0]) : f[d] = parseInt(m[0]);
            }
        }
    }, []);
    console.log("Part 1: ", Object.values(f).reduce((s,v)=>v<=1e5?v+s:s,0))
});
