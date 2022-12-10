// Read File ../input.txt

// Part 1


// ZhengLinLei

const fs = require('fs');
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    let start = 1, result = [], end = 0; 
    text.split('\s').forEach((e, i) => {
        start += +e[1]|0;
        if(!+i) result.push(...i[0]=='a'?[start,start]:[start]);
    });
    for(i in result){
        i%40-20?1:end+=result[i-1]*i;
    }

    console.log("Part 1:", end);
});