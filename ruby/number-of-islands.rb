# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
  m, n = grid.size, grid[0].size

  bfs = lambda do |u, v|
    queue = [[u, v]]

    while !queue.empty?
      x, y = queue.shift
      grid[x][y] = '0'
      [[1,0],[-1,0],[0,1],[0,-1]].each do |dx, dy|
        nx, ny = x + dx, y + dy
        if nx.between?(0, m-1) && ny.between?(0, n-1) && grid[nx][ny] == '1'
          grid[nx][ny] = '0'
          queue << [nx, ny]
        end
      end

    end
  end

  dfs = lambda do |i, j|
    return if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != '1'

    grid[i][j] = '0'
    dfs.call(i+1, j)
    dfs.call(i-1, j)
    dfs.call(i, j+1)
    dfs.call(i, j-1)
  end

  count = 0
  (0...m).each do |r|
    (0...n).each do |c|
      if grid[r][c] == '1'
        count += 1
        bfs.call(r, c)
      end
    end
  end

  count
end


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

p num_islands(grid)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

p num_islands(grid)

