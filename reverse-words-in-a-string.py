class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while right >= left and s[right] == ' ':
            right -= 1

        result = []  # 存儲反轉後的單字
        word = []    # 暫存當前單字

        for i in range(right, left - 1, -1):
            if s[i] != ' ':
                word.append(s[i])  # 累積單字
            elif word:
                # 遇到空格且 `word` 非空時，將完整單字存入 `result`
                result.append(''.join(word[::-1]))  # 手動反轉單字
                word = []

        # 避免最後沒有空格導致遺漏
        if word:
            result.append(''.join(word[::-1]))

        return ' '.join(result)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(s.split()[::-1])



sol = Solution()
print(sol.reverseWords("the sky is blue"))      # "blue is sky the"
print(sol.reverseWords("  hello world  "))      # "world hello"
print(sol.reverseWords("a good   example"))     # "example good a"
print(sol.reverseWords("     "))                # ""
print(sol.reverseWords("word"))                 # "word"

