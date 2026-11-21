from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 索引 -1 代表讀入任何元素之前的空前綴。
        first_index = {0: -1}
        remainder = 0

        for i, num in enumerate(nums):
            remainder = (remainder + num) % k

            if remainder in first_index:
                # 餘數相同代表這段總和可被 k 整除，再確認長度至少為 2。
                if i - first_index[remainder] >= 2:
                    return True
            else:
                # 保留最早的位置，讓之後能配對到最長的子陣列。
                first_index[remainder] = i

        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.checkSubarraySum([23, 2, 4, 6, 7], 6)
    assert solution.checkSubarraySum([23, 2, 6, 4, 7], 6)
    assert not solution.checkSubarraySum([23, 2, 6, 4, 7], 13)
    assert not solution.checkSubarraySum([6], 6)
    assert solution.checkSubarraySum([0, 0], 6)
    print("Examples passed")
