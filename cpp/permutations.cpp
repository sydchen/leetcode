// This is not a permutation problem, just a recursive
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int> > permute(vector<int> &seq);
    void add(vector<int> &seq, vector<int> &orig) {
        vector<int> tmp(orig.size());
        for(int k = 0; k < tmp.size(); k++) tmp[k] = orig[seq[k]];
        permutations.push_back(tmp);
    }
private:
    vector<vector<int> > permutations;
};

vector<vector<int> > Solution::permute(vector<int> &orig)
{
    vector<int> seq(orig.size());
    generate(seq.begin(), seq.end(), [&]{ return n++; });
    int len = seq.size(), i, j, cnt = 1;
    while(1) {
        add(seq, orig);
        for(i=len-2;i>=0 && seq[i]>=seq[i+1];i--)
            ;
        if(i<0)
            break;
        for(j=len-1;j>=0 && seq[j]<=seq[i];j--)
            ;
        swap(seq[i],seq[j]);

        for(i++,j=len-1;i<j;i++,j--)
            swap(seq[i],seq[j]);
        cnt++;
    }
    return permutations;
}

int main()
{
    vector<int> seq {0, -1, 1};
    Solution s;
    vector<vector<int> > permutations = s.permute(seq);
    for(auto &p:permutations) {
        copy(p.begin(), p.end(), std::ostream_iterator<int>(std::cout, " "));
        cout <<"\n";
    }
}
