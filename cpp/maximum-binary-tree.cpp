// https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C%2B%2B-O(N)-solution
#include <vector>
#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

using namespace std;

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> stk;
        for (int i = 0; i < nums.size(); ++i)
        {
            TreeNode* cur = new TreeNode(nums[i]);
            while (!stk.empty() && stk.back()->val < nums[i])
            {
                cur->left = stk.back();
                stk.pop_back();
            }
            if (!stk.empty())
                stk.back()->right = cur;
            stk.push_back(cur);
        }
        return stk.front();
    }
};

int main()
{
    vector<int> nums {3,2,1,6,0,5};
    Solution s;
    TreeNode *r = s.constructMaximumBinaryTree(nums);
    cout << r->val << "\n";
}

