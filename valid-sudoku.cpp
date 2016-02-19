#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool valid = true;
        for(int row = 0; row < 9; row++) {
            for(int col = 0; col < 9; col++) {
                if(board[row][col] == '.')
                    continue;
                valid  = checkRow(row, col, board) &&
                         checkCol(row, col, board) &&
                         checkBlock(row, col, board);
                if(!valid) {
                    return valid;
                }
            }
        }
        return valid;
    }

    bool checkRow(int row, int col, vector<vector<char>>& board) {
        for(int j = 0; j < 9; j++) {
            if(board[row][j] == board[row][col] && col != j)
                return false;
        }
        return true;
    }
    bool checkCol(int row, int col, vector<vector<char>>& board) {
        for(int i = 0; i < 9; i++) {
            if(board[i][col] == board[row][col] && row != i)
                return false;
        }
        return true;
    }
    bool checkBlock(int row, int col, vector<vector<char>>& board) {
        int block_top = floor(row / 3) * 3;
        int block_left = floor(col / 3) * 3;
        for(int i = block_top; i < block_top + 3; i++) {
            for(int j = block_left; j < block_left + 3; j++) {
                if(board[i][j] == board[row][col] && i != row && j != col)
                    return false;
            }
        }
        return true;
    }
};

int main(int argc, const char* argv[])
{
    vector<vector<char> > board = {
        {'-', 4, 5, '-', 6, 1, 2, '-', '-'},
        {'-', '-', '-', 9, 7, '-', 1, '-', 5},
        {'-', 9, '-', 5, '-', '-', '-', 6, '-'},
        {'-', '-', '-', 2, '-', '-', '-', 7, 1},
        {'-', '-', '-', '-', '-','-', '-', '-', '-'},
        {'-', '-', '-', 8, '-', '-', 6, '-', 9},
        {'-', '-', '-', '-', '-', 6, '-', '-', '-'},
        {'-', 5, 9, '-', '-', 2, '-', '-', 6},
        {'-', 7, '-', 4, '-', '-', '-', '-','-'}
    };

    Solution s;
    cout << s.isValidSudoku(board);
}
