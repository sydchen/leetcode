'''
這題要刪除最少欄位，讓整個 strs 依照 row 的順序變成字典序非遞減：
strs[0] <= strs[1] <= strs[2] <= ...

字典序比較是從左到右看：
- 如果前面某一欄已經讓 strs[i] < strs[i + 1]，那這一對 row 之後不管剩下欄位是什麼，都已經安全
- 只有目前仍然相等的相鄰 row，才需要繼續靠後面的欄位決定順序

核心想法：
從左到右貪心檢查每一欄。
如果某一欄會讓「尚未確定順序」的相鄰 row 出現 strs[i][col] > strs[i + 1][col]，
代表保留這欄一定會破壞排序，所以必須刪除。

如果這欄可以保留，就用它更新哪些相鄰 row 已經確定有序：
只要 strs[i][col] < strs[i + 1][col]，這一對 row 之後就不用再檢查。

為什麼判斷刪欄和更新 sorted_pairs 要分成兩段：
以 strs = ["ca", "bb", "ac"] 為例，第 0 欄是 c, b, a。
這欄會讓 "ca" > "bb"，所以第 0 欄必須刪除。
如果一邊檢查、一邊更新，可能會錯誤地使用「即將被刪掉的欄位」去標記某些 row 已經有序。
但被刪掉的欄位不能參與字典序判斷。
所以每一欄都要先完整確認不會造成逆序；只有確定保留後，才可以更新 sorted_pairs。

解法：Greedy
1. sorted_pairs[i] 表示 strs[i] 和 strs[i + 1] 這一對相鄰 row 是否已經確定有序
2. 逐欄 col 從左到右檢查
3. 先判斷這欄是否必須刪除：
   - 只看尚未確定有序的相鄰 row
   - 如果出現 strs[i][col] > strs[i + 1][col]，這欄要刪
4. 如果這欄不刪，再更新 sorted_pairs：
   - 若 strs[i][col] < strs[i + 1][col]，這一對 row 已經確定有序
5. 回傳刪除欄位數

為什麼 greedy 可行：
欄位是由左到右決定字典序。
如果目前欄位會讓某對尚未確定順序的相鄰 row 逆序，後面的欄位沒有機會修正，
因此這欄一定要刪。

時間複雜度：O(n * m)，n = len(strs)，m = len(strs[0])
空間複雜度：O(n)，記錄相鄰 row 是否已經確定有序
'''

class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        # sorted_pairs[i] = True 代表 strs[i] < strs[i + 1] 已經由前面的欄位決定。
        sorted_pairs = [False] * (n - 1)
        ans = 0

        for col in range(m):
            should_delete = False

            # 只檢查尚未確定有序的相鄰 row；已確定有序的 pair 後面不會再影響字典序。
            for row in range(n - 1):
                if not sorted_pairs[row] and strs[row][col] > strs[row + 1][col]:
                    should_delete = True
                    break

            if should_delete:
                ans += 1
                continue

            # 這欄可以保留，因此用它標記哪些相鄰 row 已經變成確定有序。
            for row in range(n - 1):
                if not sorted_pairs[row] and strs[row][col] < strs[row + 1][col]:
                    sorted_pairs[row] = True

        return ans


s = Solution()
print(s.minDeletionSize(["ca", "bb", "ac"]))
print(s.minDeletionSize(["xc", "yb", "za"]))
print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
