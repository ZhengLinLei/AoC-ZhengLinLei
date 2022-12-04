// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, data) => {
    let sum = 0; sum2 = 0;
    data.split('\n').map(x => x.split(',')).map(x => x.map(y => y.split('-').map(Number))).forEach(i => {
        if((i[0][0] <= i[1][0] && i[0][1] >= i[1][1]) || (i[0][0] >= i[1][0] && i[0][1] <= i[1][1])) sum ++;
        if((i[0][1] >= i[1][0] && i[0][0] <= i[1][1])) sum2 ++;
    });


    

    console.log("Part 1: ", sum);
    console.log("Part 2: ", sum2);
});
