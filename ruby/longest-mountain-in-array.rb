def longest_mountain(arr)
  n = arr.length
  return 0 if n < 3

  max_length = 0
  i = 1
  end_bound = n - 1

  while i < end_bound
    # 找到山峰的條件：arr[i] 比左右兩邊都大
    is_peak = arr[i - 1] < arr[i] && arr[i] > arr[i + 1]

    # 如果當前不是山峰，就繼續尋找
    unless is_peak
      i += 1
      next
    end

    # 找到了一個山峰，從山峰向兩側擴展
    # 1. 向左擴展，找到山的起點
    left = i - 1
    while left > 0 && arr[left - 1] < arr[left]
      left -= 1
    end

    # 2. 向右擴展，找到山的終點
    right = i + 1
    while right < end_bound && arr[right] > arr[right + 1]
      right += 1
    end

    # 3. 計算當前山的長度並更新最大值
    current_length = right - left + 1
    if current_length > max_length
      max_length = current_length
    end

    # 4. 跳躍！直接從當前山的結尾開始下一次尋找
    i = right
  end

  max_length
end

p longest_mountain([2,1,4,7,3,2,5]) # 5
p longest_mountain([2,2,2]) # 0
