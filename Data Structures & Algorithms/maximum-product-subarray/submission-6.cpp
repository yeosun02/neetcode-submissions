class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_val = nums[0], min_val = nums[0], res = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            int temp = max_val;
            max_val = max({nums[i], nums[i] * max_val, nums[i] * min_val});
            min_val = min({nums[i], nums[i] * temp, nums[i] * min_val});
            res = max(res, max_val);
        }

        return res;
    }
};
