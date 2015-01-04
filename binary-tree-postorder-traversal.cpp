#include <vector>
#include <iostream>

#ifndef NULL
#define NULL (0)
#endif

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        postorder(root);
        return traversals;
    }
    void postorder(TreeNode *node) {
        if(node == NULL)
            return;
        postorderTraversal(node->left);
        postorderTraversal(node->right);
        traversals.push_back(node->val);
    }
private:
    vector<int> traversals;
};

int main()
{
    TreeNode *node1 = new TreeNode(3);
    TreeNode *node2 = new TreeNode(2);
    TreeNode *root = new TreeNode(1);
    node2->left = node1;
    root ->right = node2;
    Solution s;
    vector<int> result = s.postorderTraversal(root);
    copy(result.begin(), result.end(), std::ostream_iterator<int>(std::cout, " "));
    delete root, node1, node2;
}
