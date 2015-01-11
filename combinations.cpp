#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        vector<vector<int> > total;
        if (k < 0 || k > n) {
            return total;
        }
        else if (k == 0) {
            total.push_back(vector<int> (1, 0));
            return total;
        }

        int lev = 0;
        int *chosen = new int[k];
        int *stack = new int[k + 1];
        vector<int> x(n);
        for(int i = 0; i < n ; i++) x[i] = i + 1;
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
};

int main()
{
    Solution sol;
    vector<vector<int> > combinations = sol.combine(1, 1);
    for(int i=0;i<combinations.size();i++) {
        copy(combinations[i].begin(), combinations[i].end(), ostream_iterator<int>(std::cout, " "));
    }
}
