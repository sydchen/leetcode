from typing import List

'''
這題要計算 nums 中有多少個 subarray 的總和剛好等於 goal。
nums 只包含 0 和 1。

核心想法：
直接用 sliding window 找「剛好等於 goal」會卡在 0，因為多個 0 會產生很多不同長度的合法 subarray。
比較穩定的做法是轉成：

剛好等於 goal 的數量 = 總和至多 goal 的數量 - 總和至多 goal - 1 的數量

例如：
- at_most(goal) 計算 sum <= goal 的 subarray 數量
- at_most(goal - 1) 計算 sum <= goal - 1 的 subarray 數量
兩者相減，剩下的就是 sum == goal。

解法：Sliding Window
1. 寫一個 at_most(max_sum) helper
2. 右指針擴張視窗，累加 nums[right]
3. 如果目前 window_sum > max_sum，就移動左指針縮窗
4. 每個 right 固定時，以 right 結尾的合法 subarray 數量是 right - left + 1

時間複雜度：O(n)
空間複雜度：O(1)
'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(max_sum: int) -> int:
            if max_sum < 0:
                return 0

            left = 0
            window_sum = 0
            count = 0

            for right in range(len(nums)):
                window_sum += nums[right]

                while window_sum > max_sum:
                    window_sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return at_most(goal) - at_most(goal - 1)


s = Solution()
print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))  # 4
print(s.numSubarraysWithSum([0, 0, 0, 0, 0], 0))  # 15
