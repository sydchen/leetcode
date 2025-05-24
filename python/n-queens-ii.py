class Solution:
    def __init__(self):
        self.colPos = [] # for eacho row, keep queen's column
        self.numSolutions = 0

    def totalNQueens(self, n: int) -> int:

        def queen(pos: int, count: int):
            if pos == n:
                if count == n:
                    self.numSolutions += 1
                    return
            else:
                for c in range(n):
                    safe = True
                    for j in range(pos):
                        if self.colPos[j] == c: # check if placed queen was in the same column
                            safe = False
                            break
                        elif abs(self.colPos[j] - c) == pos - j: # check diagonal: The x-axis distance and y-axis distance between the two queens are equal
                            safe = False
                            break
                        if not safe: break
                    if safe:
                        self.colPos[pos] = c # this column is safe to place queen
                        queen(pos + 1, count + 1) # go to next row

        self.colPos = [-1] * n
        queen(0, 0)
        return self.numSolutions

s = Solution()
print(s.totalNQueens(8)) # 92
