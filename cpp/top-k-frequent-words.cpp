// https://leetcode.com/problems/top-k-frequent-words/discuss/108366/O(nlog(k))-Priority-Queue-C++-code
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freq;
        for(auto w : words){
            freq[w]++;
        }

        auto comp = [&](const pair<string,int>& a, const pair<string,int>& b) {
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        };
        typedef priority_queue< pair<string,int>, vector<pair<string,int>>, decltype(comp) > my_priority_queue_t;
        my_priority_queue_t  pq(comp);

        for(auto w : freq ){
            pq.emplace(w.first, w.second);
            if(pq.size()>k) pq.pop();
        }

        vector<string> output;
        while(!pq.empty()){
            output.insert(output.begin(), pq.top().first);
            pq.pop();
        }
        return output;
    }

};

int main()
{
    vector<string> words {"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"};
    Solution s;
    vector<string> result = s.topKFrequent(words, 4);
    copy(result.begin(), result.end(), ostream_iterator<string>(std::cout, " "));
}
