#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int n = matrix.size();
        vector<vector<int> > tmp(n);
        for(int i = 0; i < n ; i++)
            tmp[i] = vector<int>(matrix[i]);

        int offset = 0, to_row, to_col;
        for(int col = 0; col < n ; col++) {
            for(int row = n - 1; row >= 0; row--) {
                to_row = offset / n;
                to_col = offset % n;
                matrix[to_row][to_col] = tmp[row][col];
                offset++;
            }
        }
    }
};

int main()
{
    vector<vector<int> > matrix {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Solution s;
    s.rotate(matrix);
    for(auto &i:matrix) copy(i.begin(), i.end(), std::ostream_iterator<int>(std::cout, " "));
}
