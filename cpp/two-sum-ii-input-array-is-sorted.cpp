#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        vector<int> solution;
        for(int i = 0; i < numbers.size(); i++) {
            int target_b = target - numbers[i];

            int j = i + 1, k = numbers.size() - 1;
            int mid_idx = search(numbers, i + 1, numbers.size() - 1, target_b);

            if (mid_idx > 0 && numbers[mid_idx] == target_b) {
                solution.push_back(i + 1);
                solution.push_back(mid_idx + 1);
                break;
            }
        }
        return solution;
    }

    int search(vector<int>& numbers, int i, int j, int target) {
        while(i <= j) {
            int mid_idx = (i + j) / 2;
            int mid = numbers[mid_idx];

            if (mid == target) return mid_idx;

            if (target < mid) {
                j = mid_idx - 1;
            }
            else if (target > mid) {
                i = mid_idx + 1;
            }
        }
        return -1;
    }
};

int main()
{
    Solution s;
    vector<int> numbers { -1 , 0  };
    vector<int> r = s.twoSum(numbers, -1);
    for(auto &n:r)
        cout << n << " ";
    cout << endl;
}
