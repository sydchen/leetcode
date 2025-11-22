### **維護一個變數 `miss`，代表目前能組成的數字範圍是 [1, miss)**

# * 初始：`miss = 1`

#   * 代表我們一開始還無法組出 1。
# * 若當前陣列下一個數 `nums[i]` **<= miss**：

#   * 我們就能把能組成的範圍往外擴張到 `miss + nums[i]`
#   * 並讓 `i++`
# * 若 `nums[i] > miss`：

#   * 我們就必須補(patch) 一個數字 `miss`
#   * 這樣範圍會擴張到 `miss + miss`
#   * 同時 patch 計數 `count++`

class Solution:
    def minPatches(self, nums, n):
        miss = 1
        i = 0
        patches = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1

        return patches

