#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int> &num);

private:
    void print(vector<int> &num) {
        for(int i = 0; i< num.size(); i++)
            cout << num[i];
    }
};

void Solution::nextPermutation(vector<int> &num)
{
	int len = num.size(), i, j, cnt = 0;
	while(1) {
        cnt++;
        if (cnt > 1) {
            print(num);
            break;
        }
		for(i=len-2;i>=0 && num[i]>=num[i+1];i--)
			;
		if(i<0) {
            if(cnt == 1) {
                sort(num.begin(), num.end());
                print(num);
            }
			break;
        }
		for(j=len-1;j>=0 && num[j]<=num[i];j--)
			;
		swap(num[i],num[j]);

		for(i++,j=len-1;i<j;i++,j--)
			swap(num[i],num[j]);
	}
}

int main()
{
    vector<int> num {3, 2, 1};
    Solution s;
    s.nextPermutation(num);
}
