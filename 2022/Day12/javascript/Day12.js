const fs = require("fs")

const readData = () => {
    const data = fs
        .readFileSync("../input.txt", "utf-8")
        .split(/\r?\n/)
        .map(s => s.split(""))
        .filter(Boolean)

    const [numberOfRows, numberOfCols] = [data.length, data[0].length]

    let start, end

    for (let row = 0; row < numberOfRows; row++) {
        for (let col = 0; col < numberOfCols; col++) {
            if (data[row][col] === "S") {
                start = [row, col]
                data[row][col] = "a"
            } else if (data[row][col] === "E") {
                end = [row, col]
                data[row][col] = "z"
            }
        }
    }

    return { grid: data, start, end, numberOfRows, numberOfCols }
}

const main = () => {
    const { grid, start, end, numberOfRows, numberOfCols } = readData()

    const posToStr = ([row, col]) => `${row} ${col}`
    const isPosInGrid = ([row, col]) =>
        row >= 0 && row < numberOfRows && col >= 0 && col < numberOfCols
    const isAtMostOneHigher =
        currentElevation =>
            ([row, col]) =>
                grid[row][col].charCodeAt(0) - currentElevation.charCodeAt(0) <= 1

    const DIRS = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]

    const bfs = start => {
        const queue = [[start, 0]]
        const visited = new Set([posToStr(start)])
        let res = Number.POSITIVE_INFINITY

        while (queue.length) {
            const [pos, steps] = queue.shift()

            if (posToStr(pos) === posToStr(end)) {
                res = steps
                break
            }

            DIRS.map(([dRow, dCol]) => [pos[0] + dRow, pos[1] + dCol])
                .filter(isPosInGrid)
                .filter(isAtMostOneHigher(grid[pos[0]][pos[1]]))
                .filter(pos => !visited.has(posToStr(pos)))
                .forEach(pos => {
                    visited.add(posToStr(pos))
                    queue.push([pos, steps + 1])
                })
        }

        return res
    }

    const res = bfs(start)

    console.log(res)
}

main()