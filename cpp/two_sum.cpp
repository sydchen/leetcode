#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef std::pair<int,int> Pair;

bool cmp(const Pair &a, const Pair &b)
{
    return a.first < b.first;
}

class Solution
{
    public:
        vector<int> twoSum(vector<int> &numbers, int target);
};

vector<int> Solution::twoSum(vector<int> &numbers, int target)
{
    int a, b;
    int indices[2] = {0};
    vector<Pair> pairs;
    for(int i = 0; i < numbers.size(); i++)
        pairs.push_back(Pair(numbers[i], i));

    sort(pairs.begin(), pairs.end(), cmp);
    for(int i = 0; i < pairs.size(); i++) {
        a = pairs[i].first;
        b = target - a;
        auto ib = upper_bound(pairs.begin() + i + 1, pairs.end(), Pair(b, 0), cmp);
        auto d = distance(pairs.begin(), ib);
        if(ib->first == b && d < pairs.size()) {
            indices[0] = pairs[i].second + 1, indices[1] = pairs[d].second + 1;
            break;
        }
    }

    vector<int> solution(indices, indices + 2);
    sort(solution.begin(), solution.end());
    return solution;
}

int main()
{
    Solution s;
    int myints[] = { 5, 75, 25 };
    vector<int> numbers (myints, myints + sizeof(myints) / sizeof(int) );
    vector<int> indices = s.twoSum(numbers, 100);
    cout << indices[0] << " "<<indices[1];
}
