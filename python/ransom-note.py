from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = {}
        for char in magazine:
            mag_count[char] = mag_count.get(char, 0) + 1

        for char in ransomNote:
            if mag_count.get(char, 0) > 0:
                mag_count[char] -= 1
            else:
                return False

        return True

solution = Solution()
print(solution.canConstruct("a", "b"))  # False
print(solution.canConstruct("aa", "ab"))  # False
print(solution.canConstruct("aa", "aab"))  # True
print(solution.canConstruct("hello", "hleollol"))  # True
print(solution.canConstruct("apple", "ap"))  # False

