from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        return self.find_even_numbers(digits, 3)

    def find_even_numbers(self, digits: List[int], length: int) -> List[int]:
        if length < 1 or length > len(digits):
            return []

        remaining = Counter(digits)
        result = []

        def dfs(position: int, number: int) -> None:
            if position == length:
                result.append(number)
                return

            # 個位數只試偶數。每一位都從小到大試，結果自然有序。
            choices = range(0, 10, 2) if position == length - 1 else range(10)
            for digit in choices:
                if remaining[digit] == 0:
                    continue
                if position == 0 and length > 1 and digit == 0:
                    continue

                remaining[digit] -= 1
                dfs(position + 1, number * 10 + digit)
                remaining[digit] += 1

        dfs(0, 0)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.findEvenNumbers([2, 1, 3, 0]) == [
        102, 120, 130, 132, 210, 230, 302, 310, 312, 320,
    ]
    assert solution.findEvenNumbers([2, 2, 8, 8, 2]) == [222, 228, 282, 288, 822, 828, 882]
    assert solution.findEvenNumbers([3, 7, 5]) == []
    assert solution.find_even_numbers([2, 2, 8], 2) == [22, 28, 82]
    assert solution.find_even_numbers([0, 2], 1) == [0, 2]
    print("Examples passed")
