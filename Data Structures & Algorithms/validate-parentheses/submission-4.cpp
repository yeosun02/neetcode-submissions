class Solution {
public:
    bool isValid(string s) {
        vector<char> braces;
        unordered_map<char, char> match = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                braces.push_back(match[c]);
            } else {
                if (braces.empty() || c != braces.back()) {
                    return false;
                }
                braces.pop_back();
            }
        }

        return braces.empty();
    }
};
