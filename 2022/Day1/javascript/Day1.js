// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    let data_filtered = data.split('\n');

    let sum_data = [];
    let sum = 0;

    // Foreach each item and sum it
    for(let i = 0; i < data_filtered.length; i++) {
        if(data_filtered[i] == ""){
            sum_data.push(sum);
            sum = 0;
        }else{
            sum += parseInt(data_filtered[i]);
        }
    }




    console.log("Part 1: ", Math.max(...sum_data));

    let sorted_d = sum_data.sort().reverse();
    // Sum top 3
    console.log("Part 2: " + (sorted_d[0] + sorted_d[1] + sorted_d[2]));
});



