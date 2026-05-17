'''
青蛙一開始在 point 0、lane 2，要走到最後一個 point。
每次可以：
- 往前走到下一個 point，同 lane 不算 jump
- 在同一個 point 側跳到其他 lane，算 1 次 side jump

obstacles[i] 表示 point i 哪條 lane 有障礙物，0 代表沒有障礙物。
如果某個 point 的某條 lane 有障礙物，青蛙不能站在那個位置。

核心想法：
每個 point 只需要記錄「到目前位置時，站在 lane 1 / 2 / 3 的最少 side jumps」。
因為下一步只跟目前三條 lane 的最佳狀態有關，不需要保存完整路徑。

初始狀態：
青蛙在 lane 2，所以：
- lane 1 需要先側跳 1 次才能到
- lane 2 需要 0 次
- lane 3 需要先側跳 1 次才能到
dp = [1, 0, 1]

解法：Dynamic Programming
對每個 point 從左到右處理：
1. 如果 obstacles[point] 有障礙物，先把該 lane 的 dp 設成 inf，代表不能站
2. 計算目前三條 lane 中的最小 side jumps：best = min(dp)
3. 對沒有障礙物的 lane，更新：
   dp[lane] = min(dp[lane], best + 1)
   意思是：
   - 留在原 lane：dp[lane]
   - 從其他 lane 側跳過來：best + 1
4. 最後答案是 min(dp)，代表到終點任一 lane 的最少 side jumps

為什麼這樣可行：
在同一個 point 側跳時，只要目標 lane 沒有障礙物，就可以從其他可站的 lane 跳過來。
因此每個 point 的狀態只需要三條 lane 的最小成本。

時間複雜度：O(n)，每個 point 只檢查 3 條 lane
空間複雜度：O(1)，只保存 3 條 lane 的 dp
'''

class Solution:
    def minSideJumps(self, obstacles):
        inf = 10 ** 9
        dp = [1, 0, 1]

        for obstacle in obstacles:
            # 有障礙物的 lane 不能站，先標成不可達。
            if obstacle != 0:
                dp[obstacle - 1] = inf

            best = min(dp)

            for lane in range(3):
                # 只能更新目前 point 沒有障礙物的 lane。
                if obstacle != lane + 1:
                    dp[lane] = min(dp[lane], best + 1)

        return min(dp)


s = Solution()
print(s.minSideJumps([0, 1, 2, 3, 0]))
print(s.minSideJumps([0, 1, 1, 3, 3, 0]))
print(s.minSideJumps([0, 2, 1, 0, 3, 0]))
