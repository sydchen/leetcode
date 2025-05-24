class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        len_s = len(s)
        for j in range(len(t)):
            if i < len_s and s[i] == t[j]:
                i+=1
        return i == len_s


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
print(s.isSubsequence("", "ahbgdc"))


