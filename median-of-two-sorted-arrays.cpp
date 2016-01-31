/* https://leetcode.com/discuss/15790/share-my-o-log-min-m-n-solution-with-explanation# */
/* i = 1, j = 3 */
/* 9 */
/* [3], [7, 8, 9, 10, 11, 12] */

/* i = 0, j = 4 */
/* 9 */
/* [10, 11], [3, 7, 8, 9, 12] */

/* i = 0, j = 4 */
/* 10 */
/* [20], [7, 8, 9, 10, 11, 12] */

/* i = 2, j = 2 */
/* 8.5 */
/* [3, 4], [7, 8, 9, 10, 11, 12] */

/* i = 1, j = 3 */
/* 9.5 */
/* [3], [7, 8, 9, 10, 11, 12, 13] */

/* i = 1, j = 3 */
/* 9.5 */
/* [3, 14], [7, 8, 9, 10, 11, 12] */

/* i + j = (m + n + 1) / 2 */
/* 所以左方數目會是一半或多一個, 無論m + n = 7, 左方是4個, 這時median當然是左方最大那個 */
/* 而如果 m + n = 8, 左方也是4個, 這時median當然是(左方最大 + 右方最小) / 2 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& A, vector<int>& B)
    {
        int m = A.size(), n = B.size();
        if (m > n)
            return findMedianSortedArrays(B, A);

        int minidx = 0, maxidx = m;
        int i, j, num1, num2, mid = (m + n + 1) / 2;
        while (minidx <= maxidx)
        {
            i = (minidx + maxidx) / 2;
            j = mid - i;
            if (i<m && j>0 && B[j-1] > A[i])
                minidx = i + 1;
            else if (i>0 && j<n && B[j] < A[i-1])
                maxidx = i - 1;
            else
            {
                if (i == 0)
                    num1 = B[j-1];
                else if (j == 0)
                    num1 = A[i-1];
                else
                    num1 = max(A[i-1], B[j-1]);
                break;
            }
        }
        if (((m + n) & 1))
            return num1;

        if (i == m)
            num2 = B[j];
        else if (j == n)
            num2 = A[i];
        else
            num2 = min(A[i],B[j]);

        return (num1 + num2) / 2.;
    }
};

int main(int argc, const char* argv[])
{
    vector<int> a = { 10, 11 };
    vector<int> b = { 3, 7, 8, 9, 12 };
    Solution s;
    cout << s.findMedianSortedArrays(a, b);
}
