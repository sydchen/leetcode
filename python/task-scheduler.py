'''
這題給一串 tasks 和 cooldown n。
同一種 task 之間至少要間隔 n 個時間單位。
每個時間單位可以執行一個 task，或是 idle。
目標是回傳完成所有 tasks 的最短時間。

核心想法：
最難安排的是出現次數最多的 task。
假設最多出現 max_count 次，先把它們排開：

A _ _ A _ _ A

如果 n = 2，A 之間要有 2 個空格。
max_count 個 A 會形成 max_count - 1 個空檔，每個空檔長度是 n。

如果有多個 task 都出現 max_count 次，例如 A 和 B 都出現 3 次：

A B _ A B _ A B

最後一組最高頻 task 會放在尾端，不需要再補 cooldown。

公式：
part_count = max_count - 1
part_length = n - (max_freq_tasks - 1)
empty_slots = part_count * part_length
available_tasks = len(tasks) - max_count * max_freq_tasks
idles = max(0, empty_slots - available_tasks)
answer = len(tasks) + idles

也可以理解為：
先算最高頻 task 造成的最少 idle，再把其他 task 塞進 idle 空格。
如果其他 task 夠多，idle 會被填滿，答案就是 len(tasks)。

時間複雜度：O(m)，m = len(tasks)
空間複雜度：O(1)，tasks 只有 26 種大寫英文字母
'''

from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        max_count = max(count.values())
        max_freq_tasks = sum(1 for freq in count.values() if freq == max_count)

        # 最高頻 task 之間有 max_count - 1 個空檔。
        part_count = max_count - 1

        # 每個空檔長度是 n；若有多個最高頻 task，它們會先占掉部分空位。
        part_length = n - (max_freq_tasks - 1)
        empty_slots = part_count * part_length

        available_tasks = len(tasks) - max_count * max_freq_tasks
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
