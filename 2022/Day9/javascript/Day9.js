// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

const fs = require('fs');

// Read File Async
fs.readFile('../input.txt', 'utf8', (err, text) =>  {
    let steps = {}, visited = new Set(), command = text.split('\n').map(x => x.split(/\s/)).map(x => [x[0], parseInt(x[1])]); command.forEach(x => (steps[x[0]]) ? steps[x[0]] += x[1] : steps[x[0]] = x[1]);

    const move_ = (command) => {
        let posArr = [[0, 0]];
        command.forEach(x => {
            for(let j = x[1]; j > 0; j--){
                let pos = [...posArr.at(-1)]
                switch (x[0]) {
                    case "L": pos[0] -= 1; break;
                    case "R": pos[0] += 1; break;
                    case "U": pos[1] += 1; break;
                    case "D": pos[1] -= 1; break;
                }
                posArr.push(pos);
            }
        });

        return posArr;
    };
    const follow_ = (points) => {
        let posArr = [[0, 0]];
        points.forEach((x, i) => {
            if(i < points.length - 2){
                if(Math.sqrt((points[i+1][0] - posArr[i][0])**2 + (points[i+1][1] - posArr[i][1])**2) > 1){
                    posArr.push([...x]);
                }
            }
        });

        return posArr;
    };

    console.log(follow_(move_(command)))
});