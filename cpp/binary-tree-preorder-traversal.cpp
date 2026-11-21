#include <vector>
#include <iostream>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

using namespace std;

class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> traversals;
        preorder(root, traversals);
        return traversals;
    }

private:
    void preorder(TreeNode *node, vector<int>& traversals) {
        if (node == nullptr)
            return;

        // 前序走訪：根節點 → 左子樹 → 右子樹。
        traversals.push_back(node->val);
        preorder(node->left, traversals);
        preorder(node->right, traversals);
    }
};

int main()
{
    TreeNode node1(3);
    TreeNode node2(2);
    TreeNode root(1);
    node2.left = &node1;
    root.right = &node2;
    Solution s;
    vector<int> result = s.preorderTraversal(&root);
    for (int value : result)
        cout << value << ' ';
    cout << '\n';
}
