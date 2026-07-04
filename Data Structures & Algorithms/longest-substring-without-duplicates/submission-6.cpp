class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> last_loc;
        int n = s.size();
        int longest = 0;
        int start = 0;
        for (int i = 0; i < n; ++i) {
            auto it = last_loc.find(s[i]);
            if (it != last_loc.end() && it->second >= start) {
                longest = max(longest, i - start);
                start = last_loc[s[i]] + 1;
            }

            last_loc[s[i]] = i;
        }

        longest = max(longest, n - start);
        // for (const auto& [key, val] : last_loc) { 
        //     cout << key << val << endl;
        // }
        return longest;
    }
};
