// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    let fnc = (x, n) => {
        let p = [];
        for (let i = 0; i < x.length; i++) {
            let j = p.indexOf(x[i]);  
            if(j != -1) { 
                p = p.slice(j+1); p.push(x[i]);
            }else{
                if(p.length >= n-1) return i+1
                else p.push(x[i]);
            }       
        }
    }

    console.log("Part 1:", fnc(text.split(''), 4));
    console.log("Part 2:", fnc(text.split(''), 14));
});
