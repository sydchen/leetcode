# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}

def min_ops(nums, target)
  ops = 0
  (0...(nums.size - 1)).each do |i|
    if nums[i] != target
      nums[i]   *= -1
      nums[i+1] *= -1
      ops += 1
    end
  end

  nums[-1] == target ? ops : Float::INFINITY
end

def can_make_equal(nums, k)
  [1, -1].any? { |t| min_ops(nums.dup, t) <= k }
end

p can_make_equal([1,-1,1,-1,1], 3)        # => true
p can_make_equal([-1,-1,-1,1,1,1], 5)     # => false
