#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        if (start >= 0 && start < arr.size()) {
            if (arr[start] == 0) return true;
            if (arr[start] < 0) return false;

            int v = arr[start];
            arr[start] = -v;

            return canReach(arr, start + v) || canReach(arr, start - v);
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector<int> arr = { 4,2,3,0,3,1,2 };
    cout << s.canReach(arr, 5);

    arr = { 4,2,3,0,3,1,2 };
    cout << s.canReach(arr, 0);

    arr = { 3,0,2,1,2 };
    cout << s.canReach(arr, 2);
}
