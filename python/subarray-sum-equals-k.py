from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 空前綴的總和是 0，讓從索引 0 開始的子陣列也能被計入。
        prefix_counts = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num

            # 先查詢之前的前綴和，再記錄目前的值，避免計入空子陣列。
            answer += prefix_counts.get(prefix - k, 0)
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    assert solution.subarraySum([1, -1, 1], 1) == 3
    assert solution.subarraySum([0, 0], 0) == 3
    print("Examples passed")
