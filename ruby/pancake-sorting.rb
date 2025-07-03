# @param {Integer[]} arr
# @return {Integer[]}
def pancake_sort(arr)
  res = []

  (arr.length).downto(2) do |target|
     i = arr[0...target].index(target)
     next if i == target - 1   # 它已經在正確位置

    # 如果不在最前面，先翻到前面
    if i != 0
      k1 = i + 1 # start from 1
      sub_array = arr[0, k1]
      sub_array.reverse!
      arr[0, k1] = sub_array

      res << k1
    end

    # 再把它從前面翻到 position target-1
    k2 = target
    sub_array = arr[0, k2]
    sub_array.reverse!
    arr[0, k2] = sub_array

    res << k2
  end

  res
end

p pancake_sort([3,2,4,1])
