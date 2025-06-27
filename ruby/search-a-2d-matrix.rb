# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  m = matrix.size
  return false if m == 0
  n = matrix[0].size

  left, right = 0, m * n - 1
  while left <= right
    mid = (left + right) / 2
    # 將一維索引轉回二維 (row, col)
    row = mid / n
    col = mid % n
    val = matrix[row][col]

    if val == target
      return true
    elsif val < target
      left = mid + 1
    else
      right = mid - 1
    end
  end

  false
end

puts search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
puts search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
