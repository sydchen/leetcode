#include <iostream>
#include <vector>

#ifndef NULL
#define NULL (0)
#endif

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

using namespace std;

class Solution {
public:
    ListNode *rotateRight(ListNode *head, int k) {
        if(head == NULL)
            return head;

        ListNode *tail = head, *second_to_last;
        while(tail->next) { tail = tail->next; }
        for(int i = 0; i < k; i++) {
            second_to_last = getSecondToLast(head, tail);
            tail->next = head;
            head = tail;
            tail = second_to_last;
            tail->next = NULL;
        }
        return head;
    }
private:
    ListNode* getSecondToLast(ListNode *head, ListNode *tail) {
        ListNode *second_to_last = head;
        while(second_to_last->next != tail && second_to_last->next) {
            second_to_last = second_to_last->next;
        }
        return second_to_last;
    }
};

int main()
{
    vector<ListNode *> list;
    for(int i=0; i < 1; i++)
        list.push_back(new ListNode(i + 1));
    for(int i=0; i < list.size() - 1; i++)
        list[i]->next = list[i+1];

    Solution s;
    ListNode *head = s.rotateRight(list[0], 2);
    cout << head->val;
    for(int i=0; i < list.size(); i++) delete list[i];
}
