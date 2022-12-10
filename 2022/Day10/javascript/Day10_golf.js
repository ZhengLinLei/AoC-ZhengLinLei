// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    s=1;r=[];e=0;for(i of text.split(/\s/)){
        s+=+i|0;
        if(!+i)r.push(...i[0]=='a'?[s,s]:[s]);
    }for(i in r)i%40-20?1:e+=r[i-1]*i;console.log(e);
    console.log(r.map((v,i)=>'###'[1+v-i%40]||' ').join(''));
});