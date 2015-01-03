#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int searchInsert(int A[], int n, int target) {
        auto lower = lower_bound(A, A + n, target);
        return distance(A, lower);
    }
};

int main()
{
    int A[6] = {5, 7, 7, 8, 8, 10};
    Solution s;
    int pos = s.searchInsert(A, 6, 6);
    cout << pos << endl;
}
