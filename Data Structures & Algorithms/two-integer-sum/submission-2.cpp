class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        int index = 0;
        for (int num : nums) {
            int cur_diff = target - num;
            auto it = diff.find(cur_diff);

            if (it != diff.end()) {
                return {it->second, index};
            }

            diff[num] = index++;
        }
    }
};
