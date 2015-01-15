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
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        bool last_overlap = false;
        vector<int> overlaps;
        int insert_pos = 0;
        for(int i=0; i < intervals.size(); i++) {
            if(is_overlap(intervals[i], newInterval)) {
                overlaps.push_back(i);
                last_overlap = true;
            }
            else if(last_overlap) {
                break;
            }
            else if(newInterval.end > intervals[i].start) {
                insert_pos = i + 1;
            }
        }

        if(last_overlap) {
            vector<Interval>::iterator first = intervals.begin() + overlaps.front();
            vector<Interval>::iterator last = first + overlaps.size() - 1;
            int left = first->start > newInterval.start ? newInterval.start : first->start;
            int right = last->end < newInterval.end ? newInterval.end : last->end;
            intervals.erase(first, last + 1);
            intervals.insert(first, Interval(left, right));
        }
        else {
            intervals.insert(intervals.begin() + insert_pos, newInterval);
        }

        return intervals;
    }

    bool is_overlap(Interval &a, Interval &b) {
        return (a.end >= b.start) && (b.end >= a.start);
    }
};

int main()
{
    vector<Interval> intervals { Interval(1, 5) };
    Solution s;
    vector<Interval> is = s.insert(intervals, Interval(6, 8));
    for(auto &i:is)
        cout << i.start << "  " << i.end << endl;
}
