'''
解法核心：兩段式從尾掃描

1. 第一個 while：跳過尾部空格，定位到最後一個字的末端
2. 第二個 while：計數直到遇到空格或字串開頭
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length

s = Solution()
print(s.lengthOfLastWord("Hello World"))       # 5
print(s.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(s.lengthOfLastWord("luffy is still joyboy"))  # 6
