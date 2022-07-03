#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> &x) {
    for(int n : x) cout << n << " ";
    cout << endl;
}

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int k = m + n - 1;
        m--; n--;
        while(m >= 0 && n >= 0) {
            if (nums1[m] < nums2[n])
                nums1[k--] = nums2[n--];
            else
                nums1[k--] = nums1[m--];
        }
        // most elements in nums2 are smaller than elements in nums2
        // we need to copy smaller elements to nums1
        while(n >= 0)
            nums1[k--] = nums2[n--];
    }
};

int main()
{
    Solution s;
    /* vector<int> nums1 = { 4,5,6,0,0,0 }; */
    /* vector<int> nums2 = { 1, 2, 3}; */
    /* s.merge(nums1, 3, nums2, 3); */
    vector<int> nums1 = { 1 };
    vector<int> nums2;
    s.merge(nums1, 1, nums2, 0);
    print(nums1);
}
