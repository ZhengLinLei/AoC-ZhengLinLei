// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    z=()=>text.split(/\n/).map(r=>[...r]);
    w=(m)=>m[0].map((_,i)=>m.map(r=>r[98-i]));s=z();f=z();
    for(i=0;i++<4;){
        for(y in f)for(x in f[y]) if(f[y].slice(0,x).every(v=>+v<+f[y][x])) s[y][x]='x';
        f=w(f);s=w(s);
    }console.log((""+s).split('x').length-1);
    f=text.split(/\n/).map(r=>[...r]);
    w=(m)=>m[0].map((_,i)=>m.map(r=>r[98-i]));s=f.map(r=>r.map(c=>1));
    for(i=0;i++<4;){
        for(y in f)for(x in f[y])s[y][x]*=(1+f[y].slice(+x+1).findIndex(v=>v>=f[y][x]))||98-x
        f=w(f);s=w(s);
    }console.log(Math.max(...(""+s).split(',')));
});