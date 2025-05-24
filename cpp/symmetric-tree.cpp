#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

void debug(TreeNode *node)
{
    if (node != nullptr) {
        cout << "val: " << node->val;
        if (node->left) cout << " left: " << node->left->val;
        else cout << " left (null)";
        if (node->right) cout << " right: " << node->right->val;
        else cout << " right (null)";
        cout << endl;
    }
}

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode *> q;
        q.push(root);
        q.push(root);

        while(!q.empty()) {
            TreeNode *t1 = q.front();
            q.pop();
            TreeNode *t2 = q.front();
            q.pop();

            if (t1 == nullptr && t2 == nullptr) continue;
            if (t1 == nullptr || t2 == nullptr) return false;
            if (t1->val != t2->val) return false;
            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }

        return true;
    }
};

void makeTree(int x[], int n, vector<TreeNode*> &tree)
{
    for (int i = 0; i < n; i++) {
        TreeNode *node = new TreeNode(x[i]);
        tree[i] = node;
    }

    for (int i = 0; i < n; i++) {
        int left = (i << 1) + 1;
        int right = (i << 1) + 2;
        if (left < n) tree[i]->left = tree[left];
        if (right < n) tree[i]->right = tree[right];
    }
}

int main()
{
    int x[] = { 9, -42, -42, 0, 76, 76, 0, 0, 13, 0,13 };
    int n = sizeof(x) / sizeof(int);
    vector<TreeNode *> tree (n);
    makeTree(x, n, tree);

    Solution s;
    cout << s.isSymmetric(tree[0]);

    for (int i = 0; i < n; i++) delete tree[i];
}
