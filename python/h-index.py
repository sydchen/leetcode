class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)

    def hIndex(self, citations):
        n = len(citations)
        bucket = [0] * (n + 1)

        # citations: [3,0,6,1,5]
        # bucket: [1, 1, 0, 1, 0, 2]
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        count = 0
        for i in range(n, -1, -1):
            count += bucket[i]
            if count >= i:
                return i

        return 0

s = Solution()
print(s.hIndex([3,0,6,1,5])) # 3
print(s.hIndex([0,0,0,0])) # 0
print(s.hIndex([1,3,1])) # 1

