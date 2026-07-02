class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map_s;
        for (char c : s) {
            map_s[c] = map_s[c] + 1;
        }
        
        for (char c : t) {
            if (map_s[c] == 0) {
                return false;
            }
            map_s[c] -= 1;
        }

        for (const auto& [key, val] : map_s) {
            if (val > 0) { 
                return false;
            }
        }
        return true;

    }
};
