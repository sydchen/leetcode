#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void print(ListNode *head)
{
    while(head != nullptr) {
        cout << head->val << ' ';
        head = head->next;
    }
    cout << "\n";
}

class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        ListNode *prev = nullptr, *current = head, *tmp;
        while (current) {
            tmp = current->next;
            current->next = prev;
            prev = current;
            current = tmp;
        }

        return prev;
    }
};

int main(int argc, const char* argv[])
{
    vector<ListNode *> list;
    vector<int> v = { 1, 2, 3, 4, 5 };

    for(auto x : v) {
        list.push_back(new ListNode(x));
    }
    for(int i=1; i < list.size(); i++)
        list[i-1]->next = list[i];

    print(list[0]);

    Solution s;
    ListNode *head = s.reverseList(list[0]);
    print(head);

    for(int i=0; i < list.size(); i++) delete list[i];
}

