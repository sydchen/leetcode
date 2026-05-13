'''
Bulls 是位置和數字都相同的 digit。
Cows 是數字有出現在 secret 裡，但位置不同的 digit。

重點是重複數字不能重複計算。
例如 secret = "1123", guess = "0111"：
- index 1 的 1 是 bull
- 剩下 secret 裡只有一個未配對的 1，所以 cows 只能算 1 個

解法：Counting Array
1. 同時掃過 secret 和 guess
2. 如果 secret[i] == guess[i]，這個位置是 bull，直接 bulls += 1
3. 否則把 secret[i] 和 guess[i] 分別記到兩個 10 格 count array
4. 掃完後，對每個 digit 取 min(secret_count[d], guess_count[d])
   - 這代表非 bull 的位置裡，這個 digit 最多能配成幾個 cow
5. 回傳 "{bulls}A{cows}B"

效能：
題目只有 digit 0 到 9，用固定 10 格 list 比 dict / Counter 更直接。

時間複雜度：O(n)，n = len(secret)
空間複雜度：O(1)，兩個 count array 都固定 10 格
'''

class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        secret_count = [0] * 10
        guess_count = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[ord(secret[i]) - ord('0')] += 1
                guess_count[ord(guess[i]) - ord('0')] += 1

        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return str(bulls) + 'A' + str(cows) + 'B'


s = Solution()
print(s.getHint("1807", "7810"))
print(s.getHint("1123", "0111"))
