class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n

s = Solution()

nums = [3,1,2,1,3]
k = s.removeElement(nums, 3)
print(f"k = {k}, nums = {nums}")


nums = [0,1,2,2,3,0,4,2]
k = s.removeElement(nums, 2)
print(f"k = {k}, nums = {nums}")

