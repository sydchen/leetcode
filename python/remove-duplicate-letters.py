'''
這題要刪除重複字母，讓每個字母只出現一次，並且結果字典序最小。

不能只用 set，因為相對順序很重要。
例如 s = "cbacdcbc"，答案是 "acdb"，不是單純排序後的 "abcd"。
原因是結果必須是從原字串刪除一些字元後得到的 subsequence。

核心想法：
用 stack 建立答案。
當目前字元 char 比 stack 最後一個字元更小時，如果 stack 最後一個字元後面還會再出現，
就可以先把它移除，讓較小的 char 放到更前面，使字典序變小。

但如果 stack 最後一個字元後面不會再出現，就不能移除，否則答案會缺少這個字母。

解法：Monotonic Stack
1. last_index 記錄每個字母最後一次出現的位置
2. stack 存目前建立中的答案
3. in_stack 記錄某個字母是否已經在 stack 裡，避免重複加入
4. 從左到右掃 s：
   - 如果 char 已經在 stack 裡，跳過
   - 否則，當 stack 最後一個字元比 char 大，且該字元後面還會再出現，就 pop
   - 把 char 加入 stack
5. 最後 ''.join(stack)

為什麼 greedy 可行：
字典序比較越前面的字元越重要。
只要較大的字元之後還能補回來，就應該讓目前較小的字元往前放。
這樣能讓結果更小，同時不會漏掉任何字母。

時間複雜度：O(n)，每個字元最多進 stack 一次、出 stack 一次
空間複雜度：O(1)，只有 26 個小寫字母；stack 最多 26 個字元
'''

class Solution:
    def removeDuplicateLetters(self, s):
        last_index = {}

        for i, char in enumerate(s):
            last_index[char] = i

        stack = []
        in_stack = set()

        for i, char in enumerate(s):
            if char in in_stack:
                continue

            # 若 stack 尾端較大且後面還會再出現，就先移除，讓目前較小字元提早放入。
            while stack and stack[-1] > char and last_index[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)


s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))
