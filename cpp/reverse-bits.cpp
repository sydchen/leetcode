/* https://leetcode.com/discuss/27405/o-1-bit-operation-c-solution-8ms
 *
 * Divide and Conquer bit reversal
 * 每次把上下半部對調，範圍從 16 位元縮小到 1 位元，共 5 步：
 *
 * Step1: 交換左右 16 位元
 *   ABCDEFGHIJKLMNOP QRSTUVWXYZ123456
 *   → QRSTUVWXYZ123456 ABCDEFGHIJKLMNOP
 *
 * Step2: 每 16 位元內，交換左右各 8 位元（byte）
 *   0xff00ff00 取奇數 byte，0x00ff00ff 取偶數 byte
 *
 * Step3: 每 8 位元內，交換左右各 4 位元（nibble）
 *   0xf0f0f0f0 取高 nibble，0x0f0f0f0f 取低 nibble
 *
 * Step4: 每 4 位元內，交換左右各 2 位元
 *   0xcccccccc = 11001100...，0x33333333 = 00110011...
 *
 * Step5: 每 2 位元內，交換左右各 1 位元
 *   0xaaaaaaaa = 10101010...（奇數位），0x55555555 = 01010101...（偶數位）
 *
 * 整體概念：
 *   以 16 為單位對調 → 以 8 為單位對調 → 以 4 為單位對調
 *   → 以 2 為單位對調 → 以 1 為單位對調 → 完成反轉
 *
 * 時間複雜度：O(1)，固定 5 步，比逐位處理的 O(32) 更快
 */
#include <iostream>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16) | (n << 16);                              // Step1: 交換 16 位元
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8); // Step2: 交換 8 位元
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4); // Step3: 交換 4 位元
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2); // Step4: 交換 2 位元
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1); // Step5: 交換 1 位元
        return n;
    }
};

int main(int argc, const char* argv[])
{
    Solution s;
    cout << s.reverseBits(43261596);
}
