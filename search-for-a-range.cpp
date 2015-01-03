#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> searchRange(int A[], int n, int target) {
        vector<int> result(2, -1);
        if(binary_search(A, A + n, target)) {
            auto lower = lower_bound(A, A + n, target);
            auto upper = upper_bound(A, A + n, target);
            result[0] = distance(A, lower);
            result[1] = distance(A, upper) - 1;
            return result;
        } else {
            return result;
        }
    }
};

int main()
{
    int A[6] = {5, 7, 7, 8, 8, 10};
    Solution s;
    vector<int> result = s.searchRange(A, 6, 8);
    copy(result.begin(), result.end(), std::ostream_iterator<int>(std::cout, " "));
}
