// Part 1 and Part 2

// Zheng Lin Lei

const fs = require('fs');

const pp = fs.readFileSync('../input.txt', 'utf8').trimEnd();

h=new Set();R=2e6;i=pp.split(/[^\d\-]+/);
a=Math.abs;m=([x,y,w,z])=>a(x-w)+a(y-z);
for(d=[],n=1;i[n];n+=4) {
    d.push(...[i[n],i[n+1],m(i.slice(n,n+4))]);
    if(R==i[n+3])h.add(i[n+2]);
}
for(f=-h.size,r=-1e7;r<1e7;r++)for(D=0;D<d.length;D+=3) if(m([r,R,d[D],d[D+1]])<=d[D+2]){f++;break;}console.log(f);
i=pp.split(/[^\d\-]+/);a=Math.abs;m=([x,y,w,z])=>a(x-w)+a(y-z);
for(d=[],n=1;i[n];n+=4) d.push(...[+i[n],+i[n+1],m(i.slice(n,n+4))]);
a:for(D=0;D<d.length;D+=3) for(K=0;K<=d[D+2]+1;K++){
    x=d[D]+K;y=d[D+1]+1+d[D+2]-K;
    if(Math.max(x,y)>4e6 || Math.min(x,y)<0) continue;
    for(f=G=0;!f&&G<d.length;G+=3) f=m([x,y,d[G],d[G+1]])<=d[G+2];
    if(!f) break a;
}console.log(BigInt(x)*4000000n+BigInt(y));