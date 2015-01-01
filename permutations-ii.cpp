#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num);
private:
    vector<vector<int> > permutations;
};

vector<vector<int> > Solution::permuteUnique(vector<int> &num)
{
	int len = num.size(), i, j, cnt = 1;
    sort(num.begin(), num.end());
	while(1) {
        permutations.push_back(num);
		for(i=len-2;i>=0 && num[i]>=num[i+1];i--)
			;
		if(i<0)
			break;
		for(j=len-1;j>=0 && num[j]<=num[i];j--)
			;
		swap(num[i],num[j]);

		for(i++,j=len-1;i<j;i++,j--)
			swap(num[i],num[j]);
		cnt++;
	}
    return permutations;
}

int main()
{
    vector<int> num {2, 2, 1, 1};
    Solution s;
    vector<vector<int> > permutations = s.permuteUnique(num);
    for(auto &p:permutations) {
        copy(p.begin(), p.end(), std::ostream_iterator<int>(std::cout, " "));
        cout <<"\n";
    }
}
