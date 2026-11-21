from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 最大速度可讓每堆香蕉在一小時內吃完。
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2

            # 每堆的耗時向上取整：即使剩不到 speed 根也需要一小時。
            hours = sum((pile + speed - 1) // speed for pile in piles)

            if hours <= h:
                # speed 可行，保留它並繼續尋找更小的速度。
                right = speed
            else:
                left = speed + 1

        return left


if __name__ == "__main__":
    solution = Solution()
    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert solution.minEatingSpeed([1], 1) == 1
    print("Examples passed")
