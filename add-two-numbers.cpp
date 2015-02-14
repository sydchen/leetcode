#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        saveToVector(v1, l1);
        saveToVector(v2, l2);
        int max = std::max(v1.size(), v2.size());
        int min = std::min(v1.size(), v2.size());
        appendZero(v2, max - v2.size());
        appendZero(v1, max - v1.size());

        return add();
    }
private:
    void saveToVector(vector<int> &vec, ListNode *list) {
        while(list) {
            vec.push_back(list->val);
            list = list->next;
        }
    }

    void appendZero(vector<int> &vec, int n) {
        while(n--) { vec.push_back(0); }
    }

    ListNode* add()
    {
        ListNode *head = 0, *node, *prev = 0;
        int min_length = std::min(v1.size(), v2.size());
        int carry = 0;
        for(int i=0;i<min_length;i++) {
            int sum = v1[i] + v2[i] + carry;
            node = new ListNode(sum % 10);
            if(prev)
                prev->next = node;
            else
                head = node;

            carry = sum / 10;
            prev = node;
        }

        if(carry > 0) {
            node = new ListNode(carry % 10);
            prev->next = node;
        }
        return head;
    }

    vector<int> v1, v2;
};

ListNode *makeList(const vector<int> &vec)
{
    ListNode *node, *prev = 0, *head = 0;
    for(auto n:vec) {
        node = new ListNode(n);
        if(prev) {
            prev->next = node;
        }
        else {
            head = node;
        }
        prev = node;
    }
    return head;
}

int main(int argc, const char* argv[])
{
    vector<int> x1 {1};
    vector<int> x2 {9, 9};
    ListNode *l1 = makeList(x1);
    ListNode *l2 = makeList(x2);

    Solution s;
    ListNode *head = s.addTwoNumbers(l1, l2);
    while(head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }

    while(l1 != NULL) {
        ListNode *node = l1;
        l1 = l1->next;
        delete node;
    }
    while(l2 != NULL) {
        ListNode *node = l2;
        l2 = l2->next;
        delete node;
    }
}
