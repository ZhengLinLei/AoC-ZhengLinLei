const fs = require('node:fs');
const { exit } = require('node:process');

let s = {}, map = [];
const s_ = v => {
    switch (v) {
        case '|': return [D.S, D.N];
        case '-': return [D.W, D.E];
        case 'L': return [D.N, D.E];
        case 'J': return [D.N, D.W];
        case '7': return [D.S, D.W];
        case 'F': return [D.S, D.E];
    }
    return [];
}, D = {
    N: 0,
    S: 1,
    E: 2,
    W: 3
}, dir = [
    {x: 0, y: -1},
    {x: 0, y: 1},
    {x: 1, y: 0},
    {x: -1, y: 0},
]

try {
    map = fs.readFileSync('../in', 'utf8').split("\n").map((line, y) => line.split('').map((v, x) => {
        if (v == 'S') s = {x: x, y: y}
        return {
            v: v,
            links: s_(v)
        }
    }));
} catch (err) {
    console.error(err);
    exit();
}



let a_ = [];
if (s.x > 0 && map[s.y][s.x-1].links.includes(D.E)) a_.push(D.W);
if (s.x < map[0].length-1 && map[s.y][s.x+1].links.includes(D.W)) a_.push(D.E);
if (s.y > 0 && map[s.y-1][s.x].links.includes(D.S)) a_.push(D.N);
if (s.y < map.length-1 && map[s.y+1][s.x].links.includes(D.N)) a_.push(D.S);
map[s.y][s.x].links = a_;

let stack = [];
stack.push({p: s, dist: 0});

while (stack.length) {
    let n = stack.shift();
    if (map[n.p.y][n.p.x].dist === undefined || map[n.p.y][n.p.x].dist > n.dist) {
        map[n.p.y][n.p.x].dist = n.dist;
        map[n.p.y][n.p.x].links.forEach(d => {
            stack.push({
                p: {x: n.p.x + dir[d].x, y: n.p.y + dir[d].y},
                dist: n.dist+1
            })
        })
    }
}

console.log('Part 1:', Math.max(...map.flat().map(p => p.dist === undefined ? 0 : p.dist)));

let m = Array(map.length*3);
let mD = Array(map.length*3);

map.forEach((row, y) => row.forEach((v, x) => {
    let submap = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]];
    if (v.dist === undefined) submap[1][1] = 2;
    else {
        submap[1][1] = 1; // impassable
        v.links.forEach(d => {
            submap[1 + dir[d].y][1 + dir[d].x] = 1;
        })
    }

    for (let i = 0; i <= 2; i++) {
        if (m[y*3+i] === undefined) {
            m[y*3+i] = Array(map[0].length*3);
            mD[y*3+i] = Array(map[0].length*3);
        }
        for (let j = 0; j <= 2; j++) {
            m[y*3+i][x*3+j] = submap[i][j];
        }
    }
}))

stack = [];

for (let x = 0; x < map[0].length; x++) {
    if (map[0][x].dist === undefined) stack.push({p: {x: x*3, y: 0}, dist: 0});
    if (map[map.length-1][x].dist === undefined) stack.push({p: {x: x*3, y: (map.length-1)*3}, dist: 0});
}

for (let y = 1; y < map.length-1; y++) {
    if (map[y][0].dist === undefined) stack.push({p: {x: 0, y: y*3}, dist: 0});
    if (map[y][map[0].length-1].dist === undefined) stack.push({p: {x: (map[0].length-1)*3, y: y*3}, dist: 0});
}

while (stack.length) {
    let n = stack.shift();
    if (m[n.p.y] !== undefined && m[n.p.y][n.p.x] !== undefined && m[n.p.y][n.p.x] !== 1 && mD[n.p.y][n.p.x] === undefined && (mD[n.p.y][n.p.x] === undefined || mD[n.p.y][n.p.x] > n.dist)) {
        mD[n.p.y][n.p.x] = n.dist;
        dir.forEach(d => stack.push({
            p: {x: n.p.x + d.x, y: n.p.y + d.y},
            dist: n.dist+1
        }))
    }
}

let sum = 0;

map.forEach((row, y) => row.forEach((v, x) => {
    if (v.dist === undefined && mD[y*3][x*3] === undefined) sum++;
}))

console.log('Part 2:', sum);

