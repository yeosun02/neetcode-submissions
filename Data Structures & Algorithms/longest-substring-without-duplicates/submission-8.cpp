class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> last_loc;
        int longest = 0;
        int l = 0;
        for (int r = 0; r < s.size(); ++r) {
            auto it = last_loc.find(s[r]);
            if (it != last_loc.end()) {
                l = max(l, it->second + 1);
            }

            last_loc[s[r]] = r;
            longest = max(longest, r - l + 1);
        }

        return longest;
    }
};
