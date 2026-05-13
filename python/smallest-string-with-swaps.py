'''
pairs 表示哪些 index 可以互相交換，而且交換可以做任意多次。
如果 0 可以和 3 換、3 可以和 2 換，那 0、2、3 其實屬於同一個連通群，
這個群裡的字元可以透過多次交換任意重排。

因此問題可以拆成：
1. 找出所有可以互相交換的 index 群組
2. 對每個群組，把群組裡的字元排序
3. 把較小的字元放到群組裡較小的 index，得到字典序最小結果

解法：Union-Find
1. 每個 index 一開始都是自己的 parent
2. 對 pairs 裡的每組 [a, b] 做 union，將可互換的 index 合併成同一群
3. 掃過 s，把相同 root 的 index 收集到同一個 list
4. 對每個群組：
   - indices 本身是由小到大掃描收集，所以已經是遞增
   - chars = sorted(s[i] for i in indices)
   - 依序把最小字元放回最小 index

效能：
Union-Find 使用 path compression 和 union by size，讓 find / union 接近 O(1)。
每個群組排序的總成本最多是 O(n log n)。

時間複雜度：O((n + p) * α(n) + n log n)，n = len(s)，p = len(pairs)
空間複雜度：O(n)
'''

from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            # Path compression：查 root 的同時，把沿路節點直接接到更上層，降低後續查找成本。
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            # Union by size：小集合接到大集合，避免樹太深。
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

        for a, b in pairs:
            # 每個 pair 代表兩個 index 所在的群組可以合併。
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            # 同一個 root 的 index 可以互相交換，收成同一組處理。
            groups[find(i)].append(i)

        ans = list(s)

        for indices in groups.values():
            # indices 是由小到大掃描收集；把排序後的字元依序放回，字典序會最小。
            chars = sorted(ans[i] for i in indices)

            for i, char in zip(indices, chars):
                ans[i] = char

        return ''.join(ans)


class Solution2:
    '''
    比較直觀的版本：把 pairs 當成無向圖。
    兩個 index 之間有邊，代表這兩個位置可以直接交換。
    如果多個 index 連在一起，代表它們在同一個 connected component 裡，字元可以任意重排。
    '''
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        graph = [[] for _ in range(n)]

        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        ans = list(s)
        visited = [False] * n

        for start in range(n):
            if visited[start]:
                continue

            # 用 DFS 找出和 start 相連的所有 index，也就是一個可互換群組。
            stack = [start]
            visited[start] = True
            indices = []

            while stack:
                node = stack.pop()
                indices.append(node)

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            # 同一群組裡的字元可任意重排；最小字元放最小 index，字典序會最小。
            indices.sort()
            chars = sorted(ans[i] for i in indices)

            for i, char in zip(indices, chars):
                ans[i] = char

        return ''.join(ans)


s = Solution()
print(s.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))
print(s.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]))
print(s.smallestStringWithSwaps("cba", [[0, 1], [1, 2]]))

s2 = Solution2()
print(s2.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))
print(s2.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]))
print(s2.smallestStringWithSwaps("cba", [[0, 1], [1, 2]]))
