class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int value = n * (n + 1) / 2;
        for (int num : nums) {
            value -= num;
        }
        return value;
    }
};
