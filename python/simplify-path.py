'''
將 Unix 路徑簡化為標準形式。

規則：
- "."  → 當前目錄，忽略
- ".." → 上一層目錄，pop stack
- 多個連續 "/" → 視為單一 "/"
- 空字串（split 後的空元素）→ 忽略

解法：Stack
按 "/" split 後逐一處理每個元素：
- 空字串或 "." → 跳過
- ".."          → pop（若 stack 不為空）
- 其他          → push

最後用 "/" join stack，加上開頭的 "/"。

時間複雜度：O(n)
空間複雜度：O(n)
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)

s = Solution()
print(s.simplifyPath("/home/"))           # /home
print(s.simplifyPath("/home//foo/"))      # /home/foo
print(s.simplifyPath("/home/user/Documents/../Pictures"))  # /home/user/Pictures
print(s.simplifyPath("/../"))             # /（根目錄不能再往上）
print(s.simplifyPath("/.../a/../b/c/../d/./"))  # /.../b/d（...是合法目錄名）
