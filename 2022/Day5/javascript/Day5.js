// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    let sum = '', stack_data = [], data = text.split('\n\n'), stack =  data[0].split('\n').slice(0, -1).map(x => x.split('')).reduce((prev, next) => next.map((item, i) => (prev[i] || []).concat(next[i])), []).map(x => x.reverse()), command_data =  data[1].split('\n').map(x => x.split(/move\s|\sfrom\s|\sto/).slice(1).map(s => parseInt(s)));
    for (let i = 1; i < stack.length; i += 4) stack_data.push(stack[i].filter(x => x != ' '));

    let stack_data1 = stack_data.map(x => x.slice());
    command_data.forEach(x => {
        stack_data1[x[2]-1] = stack_data1[x[2]-1].concat(stack_data1[x[1]-1].slice(x[0]*-1).reverse());
        stack_data1[x[1]-1] = stack_data1[x[1]-1].slice(0, x[0]*-1);
    });
    stack_data1.forEach(x => sum += x[x.length-1]);
    // Part 1
    console.log('Part 1:', sum)
    
    let sum2 = '', stack_data2 = stack_data.map(x => x.slice());
    command_data.forEach(x => {
        stack_data2[x[2]-1] = stack_data2[x[2]-1].concat(stack_data2[x[1]-1].slice(x[0]*-1));
        stack_data2[x[1]-1] = stack_data2[x[1]-1].slice(0, x[0]*-1);
    });
    stack_data2.forEach(x => sum2 += x[x.length-1]);
    // Part 2
    console.log('Part 2:', sum2)
});
