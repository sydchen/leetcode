class Solution(object):
    def mirrorReflection(self, p, q):
        while p % 2 == 0 and q % 2 == 0: p, q =  p / 2, q / 2
        if p % 2 == 0:
            return 2;
        elif q % 2 == 0:
            return 0;
        else:
            return 1;

s = Solution()
x = s.mirrorReflection(2, 1)
print(x)

