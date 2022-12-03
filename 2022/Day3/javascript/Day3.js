// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, data) => {
    let letter_arr = [], sum = 0; data.split('\n').map(x => [x.substring(0, x.length / 2), x.substring(x.length / 2, x.length)]).forEach(i => {
        for (let j = 0; j < i[0].length; j++) {
            if(i[1].indexOf(i[0][j]) != -1){
                letter_arr.push(i[0][j]);
                break;
            }
        }
    });
    letter_arr.forEach(el => sum += (el.toUpperCase() === el) ? el.charCodeAt() - 38 : el.charCodeAt() - 96);


    console.log("Part 1: ", sum);


    // ===========
    let letter_arr2 = [], sum2 = 0; data.split('\n').reduce((arr, el, i) => { 
        const i2 = Math.floor(i/3);
        if(!arr[i2]) arr[i2] = [];
        arr[i2].push(el);
        return arr
      }, []).forEach(i => {
        for (let j = 0; j < i[0].length; j++) {
            if(i[1].indexOf(i[0][j]) != -1 && i[2].indexOf(i[0][j]) != -1){
                letter_arr2.push(i[0][j]);
                break;
            }
        }
    });

    letter_arr2.forEach(el => sum2 += (el.toUpperCase() === el) ? el.charCodeAt() - 38 : el.charCodeAt() - 96);
    
    console.log("Part 2: ", sum2);
});
