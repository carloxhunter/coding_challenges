#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> ht;
        vector<vector<string>> ans;
        for (auto it = begin(strs); it != end(strs); ++it)
        {
            string key = *it;
            sort(key.begin(), key.end());
            if (ht.find(key) == ht.end())
            {
                ht[key] = {*it};
            }
            else
            {
                ht[key].push_back(*it);
            }
        }
        for (auto it = begin(ht); it != end(ht); ++it)
        {
            ans.push_back(it->second);
        }
        return ans;
    }
};

int main()
{
    vector<string> testcase1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
    Solution S;
    vector<vector<string>> sol = S.groupAnagrams(testcase1);

    for (auto it = begin(sol); it != end(sol); ++it)
    {
        cout << "<--------space-------->" << endl;
        for (auto its = begin(*it); its != end(*it); ++its)
        {
            cout << *its << " " << endl;
        }
    }

    return 0;
}