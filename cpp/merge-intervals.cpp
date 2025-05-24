/* https://leetcode.com/discuss/49276/c-10-line-solution-easing-understanding */
#include <iostream>
#include <vector>

using namespace std;

struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> merged;
        if(intervals.empty())
            return merged;

        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b){return a.start < b.start;});

        merged.push_back(intervals[0]);
        for(int i = 1; i < intervals.size(); i++) {
            if(merged.back().end < intervals[i].start)
                merged.push_back(intervals[i]);
            else
                merged.back().end = max(intervals[i].end, merged.back().end);
        }
        return merged;
    }
};

int main(int argc, const char* argv[])
{
	vector<Interval> intervals { Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18) };
    Solution s;
    vector<Interval> merged = s.merge(intervals);

    for(const auto &m : merged)
        cout << m.start << " " << m.end <<endl;
}
