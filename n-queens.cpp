#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        Solution(): total_sol(0) {}
        vector<vector<string> > solveNQueens(int n)
        {
            n_rows = n;
            queen.resize(n_rows);
            eightQueen(0);
            return solutions;
        }
        void eightQueen(int row);
        bool chkQueen(int row);
        int totalNQueens(int n) {
            solveNQueens(n);
            return total_sol;
        }

    private:
        int total_sol, n_rows;
        vector<int> queen;
        vector<vector<string> > solutions;
};

void Solution::eightQueen(int row)
{
    if(row == n_rows) {
        total_sol += 1;
        vector<string> currentSol;
        for(int row = 0; row < n_rows; row++) {
            string s(n_rows, '.');
            s[queen[row]] = 'Q';
            currentSol.push_back(s);
        }
        solutions.push_back(currentSol);
    }
    else {
        for(int i = 0; i < n_rows; i++) {
            queen[row] = i;
            if(chkQueen(row)) eightQueen(row + 1);
        }
    }
}

bool Solution::chkQueen(int row)
{
    for(int i = 1; i <= row; i++) {
        if(queen[i-1] == queen[row]) return false;
        if(queen[row-i] == queen[row] + i) return false;
        if(queen[row-i] == queen[row] - i) return false;
    }
    return true;
}

int main()
{
    Solution sol;
    /* sol.solveNQueens(8); */
    cout << sol.totalNQueens(8);
}
