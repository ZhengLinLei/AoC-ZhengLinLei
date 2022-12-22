defmodule Day22 do
  @moduledoc """
  This solution is hard-coded for a cube which looks like this:
  -----
  | 12|
  | 3 |
  |54 |
  |6  |
  -----
  """
  require Logger

  def solve1() do
    solve(&simple/2)
  end

  def solve2() do
    solve(&cube/2)
  end

  def solve(clamper) do
    lines = Input.get_lines(22, "")
    {map, [_, directions]} = Enum.split_while(lines, &(&1 != ""))

    dirs = Regex.split(~r{[LR]}, directions, include_captures: true)
    Logger.warn("Dirs are #{inspect(dirs)}")

    points = parse_map(map)

    start_col = find_bounds(:row, 0, points) |> elem(0)
    {dir, row, col} = move({:right, 0, start_col}, dirs, points, clamper)
    ord(dir) + (row + 1) * 1000 + (col + 1) * 4
  end

  def find_bounds(:row, i, points) do
    relevant = points |> Map.keys() |> Enum.filter(&(elem(&1, 0) == i)) |> Enum.map(&elem(&1, 1))
    {Enum.min(relevant), Enum.max(relevant)}
  end

  def find_bounds(:col, i, points) do
    relevant = points |> Map.keys() |> Enum.filter(&(elem(&1, 1) == i)) |> Enum.map(&elem(&1, 0))
    {Enum.min(relevant), Enum.max(relevant)}
  end

  def parse_map(lines) do
    lines
    |> Enum.with_index()
    |> Enum.reduce(%{}, &parse_line/2)
  end

  def parse_line({line, row}, points) do
    line
    |> String.to_charlist()
    |> Enum.with_index()
    |> Enum.filter(&(elem(&1, 0) != 32))
    |> Enum.reduce(points, fn {ch, j}, acc -> Map.put(acc, {row, j}, ch) end)
  end

  def next(:left), do: :up
  def next(:up), do: :right
  def next(:right), do: :down
  def next(:down), do: :left

  def ord(:right), do: 0
  def ord(:down), do: 1
  def ord(:left), do: 2
  def ord(:up), do: 3

  def move(state, [], _points, _clamper) do
    Logger.warn("Done at #{inspect(state)}")
    state
  end

  def move({dir, row, col}, ["R" | dirs], points, clamper) do
    # Logger.warn("Turning right from #{inspect({dir, row, col})}")
    move({next(dir), row, col}, dirs, points, clamper)
  end

  def move({dir, row, col}, ["L" | dirs], points, clamper) do
    # Logger.warn("Turning left from #{inspect({dir, row, col})}")
    move({next(next(next(dir))), row, col}, dirs, points, clamper)
  end

  def move(state, [numstr | dirs], points, clamper) do
    # Logger.warn("Moving forward #{numstr} from #{inspect(state)}")
    forward(state, String.to_integer(numstr), dirs, points, clamper)
  end

  def forward(state, 0, dirs, points, clamper) do
    move(state, dirs, points, clamper)
  end

  def forward({:left, row, col} = state, i, dirs, points, clamper) do
    {newdir, newrow, newcol} = clamper.(row, col - 1)
    newdir = newdir || :left

    if Map.fetch!(points, {newrow, newcol}) != ?. do
      move(state, dirs, points, clamper)
    else
      forward({newdir, newrow, newcol}, i - 1, dirs, points, clamper)
    end
  end

  def forward({:right, row, col} = state, i, dirs, points, clamper) do
    {newdir, newrow, newcol} = clamper.(row, col + 1)
    newdir = newdir || :right

    if Map.fetch!(points, {newrow, newcol}) != ?. do
      move(state, dirs, points, clamper)
    else
      forward({newdir, newrow, newcol}, i - 1, dirs, points, clamper)
    end
  end

  def forward({:down, row, col} = state, i, dirs, points, clamper) do
    {newdir, newrow, newcol} = clamper.(row + 1, col)
    newdir = newdir || :down

    if Map.fetch!(points, {newrow, newcol}) != ?. do
      move(state, dirs, points, clamper)
    else
      forward({newdir, newrow, newcol}, i - 1, dirs, points, clamper)
    end
  end

  def forward({:up, row, col} = state, i, dirs, points, clamper) do
    {newdir, newrow, newcol} = clamper.(row - 1, col)
    newdir = newdir || :up

    if Map.fetch!(points, {newrow, newcol}) != ?. do
      move(state, dirs, points, clamper)
    else
      forward({newdir, newrow, newcol}, i - 1, dirs, points, clamper)
    end
  end

  ##### Left sides

  def simple(row, 49) when row < 50 do
    {nil, row, 149}
  end

  def simple(row, 49) when row < 100 do
    {nil, row, 99}
  end

  def simple(row, -1) when row < 150 do
    {nil, row, 99}
  end

  def simple(row, -1) do
    {nil, row, 49}
  end

  def cube(row, 49) when row < 50 do
    # left of 1 --> left of 5
    {:right, 149 - row, 0}
  end

  def cube(row, 49) when row < 100 do
    # left of 3 --> top of 5
    {:down, 100, row - 50}
  end

  def cube(row, -1) when row < 150 do
    # left of 5 --> left of 1
    {:right, 49 - (row - 100), 50}
  end

  def cube(row, -1) do
    # left of 6 --> top of 1
    {:down, 0, 50 + (row - 150)}
  end

  #### Top sides

  def simple(-1, col) when col < 100 do
    {nil, 149, col}
  end

  def simple(-1, col) do
    {nil, 49, col}
  end

  def simple(99, col) when col < 50 do
    {nil, 199, col}
  end

  def cube(-1, col) when col < 100 do
    # top of 1 --> left of 6
    {:right, col - 50 + 150, 0}
  end

  def cube(-1, col) do
    # top of 2 --> bottom of 6
    {:up, 199, col - 100}
  end

  def cube(99, col) when col < 50 do
    # top of 5 --> left of 3
    {:right, 50 + col, 50}
  end

  #### Right sides

  def simple(row, 150) do
    {nil, row, 50}
  end

  def simple(row, 100) when row >= 100 do
    {nil, row, 0}
  end

  def simple(row, 100) when row >= 50 do
    {nil, row, 50}
  end

  def simple(row, 50) when row >= 150 do
    {nil, row, 0}
  end

  def cube(row, 150) do
    # right of 2 --> right of 4 (UD)
    {:left, 149 - row, 99}
  end

  def cube(row, 50) when row >= 150 do
    # right of 6 --> bottom of 4
    {:up, 149, 50 + (row - 150)}
  end

  def cube(row, 100) when row >= 100 do
    # right of 4 --> right of 2
    {:left, 49 - (row - 100), 149}
  end

  def cube(row, 100) when row >= 50 do
    # right of 3 --> bottom of 2
    {:up, 49, 100 + (row - 50)}
  end

  #### Bottom sides

  def simple(200, col) do
    {nil, 100, col}
  end

  def simple(150, col) when col >= 50 do
    {nil, 0, col}
  end

  def simple(50, col) when col >= 100 do
    {nil, 0, col}
  end

  def cube(200, col) do
    # bottom of 6 --> top of 1
    {:down, 0, 100 + col}
  end

  def cube(150, col) when col >= 50 do
    # bottom of 4 --> right of 6
    {:left, 150 + (col - 50), 49}
  end

  def cube(50, col) when col >= 100 do
    # bottom of 2 --> right of 3
    {:left, col - 100 + 50, 99}
  end

  def simple(r, c) do
    {nil, r, c}
  end

  def cube(r, c) do
    {nil, r, c}
  end
end
