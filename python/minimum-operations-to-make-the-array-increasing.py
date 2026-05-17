'''
這題每次操作可以把任一元素加 1。
目標是用最少操作次數，讓 nums 變成 strictly increasing：
nums[0] < nums[1] < nums[2] < ...

核心想法：
從左到右處理時，nums[i] 只需要比前一個數字大 1。
如果 nums[i] 已經大於前一個數字，就不用動。
如果 nums[i] <= previous，就必須把 nums[i] 增加到 previous + 1。

為什麼只增加到 previous + 1：
strictly increasing 的最低要求就是 nums[i] > previous。
能滿足條件的最小值是 previous + 1。
加到更大雖然也合法，但會增加操作次數，還會讓後面的數字更難滿足條件。

解法：Greedy
1. previous 記錄目前處理完後，前一個位置的值
2. 從 nums[1] 開始往右掃
3. 如果 nums[i] <= previous：
   - target = previous + 1
   - ans += target - nums[i]
   - previous = target
4. 如果 nums[i] > previous：
   - previous = nums[i]
5. 回傳 ans

時間複雜度：O(n)，n = len(nums)
空間複雜度：O(1)
'''

class Solution:
    def minOperations(self, nums):
        ans = 0
        previous = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= previous:
                # 只增加到 previous + 1，剛好滿足嚴格遞增，操作次數最少。
                target = previous + 1
                ans += target - nums[i]
                previous = target
            else:
                previous = nums[i]

        return ans


s = Solution()
print(s.minOperations([1, 1, 1]))
print(s.minOperations([1, 5, 2, 4, 1]))
print(s.minOperations([8]))
