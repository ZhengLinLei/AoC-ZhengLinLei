// Part 1 and Part 2

// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    f={};text.split(/\n/).reduce((d,l)=>{
        if(m=l.match(/d (.+)/)){
            d=m[1]=='..'?d.match(/(.+\/).*\//)[1]:d+m[1]+'/';
            f[d]|=0;
        }
        if(m=l.match(/\d+/)) for(k in f)f[k]+=d.includes(k)?+m[0]:0;
        return d;
    },'');console.log(Object.values(f).reduce((s,v)=>v<=1e5?v+s:s,0))
    
    f={};g={};text.split(/\n/).reduce((d,l)=>{
        if(m=l.match(/d (.+)/)){
            d=m[1]=='..'?d.match(/(.+\/).*\//)[1]:d+m[1]+'/';
            f[d]|=0;
        }
        if(m=l.match(/\d+/))for(k in f)f[k]+=d.includes(k)?+m[0]:0;
        return d;
    },'');console.log(Math.min(...Object.values(f).filter(v=>v>f['//']-4e7)))
});