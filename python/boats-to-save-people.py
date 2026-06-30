'''
這題每艘船最多載兩個人，且重量總和不能超過 limit。
要用最少船數救完所有人。

核心想法：
先排序 people。
每次優先處理最重的人，因為最重的人最難配對。
如果最重的人可以和最輕的人同船，就讓他們一起走。
否則最重的人只能自己坐一艘船。

解法：Sort + Two Pointers
1. people 由小到大排序
2. left 指向最輕的人，right 指向最重的人
3. 每一輪都使用一艘船載走 right
4. 如果 people[left] + people[right] <= limit，left 也一起上船
5. right 一定會往左移，直到所有人都被處理

為什麼可行：
最重的人如果不能和最輕的人配對，就不可能和其他更重的人配對，只能單獨坐船。
如果可以和最輕的人配對，這樣也不會浪費容量，因為最輕的人最好被配掉。

時間複雜度：O(n log n)
空間複雜度：O(1)，不含排序使用的額外空間
'''

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats


s = Solution()
print(s.numRescueBoats([1, 2], 3))
print(s.numRescueBoats([3, 2, 2, 1], 3))
print(s.numRescueBoats([3, 5, 3, 4], 5))

