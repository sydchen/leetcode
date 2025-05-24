#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int> > combine(vector<int> & x, int k);
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end());
        vector<vector<int> > total;
        for(int k=0;k<=S.size();k++) {
            vector<vector<int> > result = combine(S, k);
            copy(result.begin(), result.end(), back_inserter(total));
        }
        return total;
    }
};

vector<vector<int> > Solution::combine(vector<int> &x, int k)
{
    int n = x.size();
    vector<vector<int> > total;
    if (k < 0 || k > n) {
        return total;
    }
    else if (k == 0) {
        total.push_back(vector<int>());
        return total;
    }

    int lev = 0;
    int *chosen = new int[k];
    int *stack = new int[k + 1];
    for(int i = 0; i <= k; i++) stack[i] = 0;
    stack[0] = -1;

    for(;;) {
        chosen[lev] = x[stack[lev + 1]];
        for(lev++; lev < k; lev++)
            chosen[lev] = x[stack[lev+1] = stack[lev]+1];

        total.push_back(vector<int>(chosen, chosen + k));

        do {
            if (lev == 0) return total;
            stack[lev--]++;
        } while (stack[lev + 1] + k == n + lev + 1);
    }

    delete []chosen;
    delete []stack;
    return total;
}

int main()
{
    vector<int> set {4, 1, 0};
    Solution sol;
    vector<vector<int> > subsets = sol.subsets(set);
    for(int i=0;i<subsets.size();i++) {
        printf("[");
        copy(subsets[i].begin(), subsets[i].end(), ostream_iterator<int>(std::cout, " "));
        printf("]\n");
    }
}
