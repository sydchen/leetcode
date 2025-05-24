class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1
        
        return all(x == 0 for x in count)


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
