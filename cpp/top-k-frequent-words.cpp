// https://leetcode.com/problems/top-k-frequent-words/discuss/108366/O(nlog(k))-Priority-Queue-C++-code
#include <algorithm>
#include <iostream>
#include <iterator>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freq;
        for (const auto& word : words) {
            ++freq[word];
        }
    
        vector<string> uniqueWords;
        uniqueWords.reserve(freq.size());
    
        for (const auto& [word, _] : freq) {
            uniqueWords.push_back(word);
        }
    
        sort(uniqueWords.begin(), uniqueWords.end(), [&](const string& a, const string& b) {
            if (freq[a] != freq[b]) {
                return freq[a] > freq[b];
            }
            return a < b;
        });
    
        uniqueWords.resize(k);
        return uniqueWords;
    }
};

int main() {
    vector<string> words {"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"};
    Solution s;
    vector<string> result = s.topKFrequent(words, 4);
    copy(result.begin(), result.end(), ostream_iterator<string>(std::cout, " "));
}
