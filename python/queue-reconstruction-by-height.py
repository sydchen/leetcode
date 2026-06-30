'''
這題每個人用 [h, k] 表示：
- h 是身高
- k 是在這個人前面，身高 >= h 的人數

目標是重建符合所有 [h, k] 條件的 queue。

核心想法：
先處理高的人，再處理矮的人。
因為矮的人不會影響高的人的 k 值；但高的人會影響矮的人的 k 值。

排序規則：
1. 身高 h 由高到低
2. 如果身高相同，k 由小到大

排序後，逐一把人插入答案的 index = k 位置。
因為目前答案裡的人都比當前的人高或一樣高，所以插到 k 位置時，
前面剛好會有 k 個身高 >= h 的人。

例如：
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
排序後：
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

依序插入：
[7,0] 插 index 0 -> [[7,0]]
[7,1] 插 index 1 -> [[7,0],[7,1]]
[6,1] 插 index 1 -> [[7,0],[6,1],[7,1]]
後面插入較矮的人，不會破壞前面較高人的 k 值。

時間複雜度：O(n^2)，排序 O(n log n)，list insert 最差 O(n)
空間複雜度：O(n)
'''

class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda person: (-person[0], person[1]))
        ans = []

        for person in people:
            # 目前 ans 裡的人都比 person 高或一樣高，所以 k 就是 person 應插入的位置。
            ans.insert(person[1], person)

        return ans


s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
