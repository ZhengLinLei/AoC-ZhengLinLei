// Read File ../input.txt

// Part 1


// ZhengLinLei

const fs = require('fs');

const Rules = {
    "X": 1, "A": 1,
    "Y": 2, "B": 2,
    "Z": 3, "C": 3,
}
// Points added if you won or not
const Rules2 = {
    "-1": 0, "X": 0,
    "0": 3,  "Y": 3,
    "1": 6,  "Z": 6,
}

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    let data_filtered = data.split('\n').map(x => x.split(' '));

    let sumPoints = 0;
    data_filtered.forEach(el => sumPoints += Rules2[(Rules[el[1]] - Rules[el[0]] == -2) ? 1 : ((Rules[el[1]] - Rules[el[0]] == 2) ? -1 : (Rules[el[1]] - Rules[el[0]]))] + Rules[el[1]]);

    console.log("Part 1: ", sumPoints);
});
