# 8 ms
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # 用 set 加速查找
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case：空字串可分割

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # 找到一組就可以提早退出這層迴圈

        return dp[n]

'''
0ms

s[j:i] in word_set => word_set.__contains__(s[j:i]) => word_in(s_str[j:i])
dp[i] = True => dp.__setitem__(i, True) => dp_i(i, True)
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        # 只保留字典中不同的長度
        lengths = list({len(w) for w in wordDict})
        n = len(s)

        # dp[i] 表示 s[:i] 是否能被切分
        dp = [False] * (n + 1)
        dp[0] = True

        # 把常用變數拉到局部，加速屬性存取
        dp_i = dp.__setitem__
        dp_arr = dp
        s_str = s
        word_in = word_set.__contains__

        for i in range(1, n + 1):
            for L in lengths:
                j = i - L
                if j >= 0 and dp_arr[j] and word_in(s_str[j:i]):
                    dp_i(i, True)
                    break

        return dp_arr[n]


s = Solution()
print(s.wordBreak("leetcode", ["leet","code"]))
print(s.wordBreak("applepenapple", ["apple","pen"]))
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False
