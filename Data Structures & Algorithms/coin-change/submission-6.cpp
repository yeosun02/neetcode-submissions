class Solution {
public:       
    int dfs(int amt, vector<int>& dp, int amount, vector<int>& coins) {
        if (amt < 0) { 
            return -1;
        }
        if (dp[amt] < amount + 1) {
            return dp[amt];
        }

        int cur_min = amount + 1;
        for (int coin : coins) {
            int res = dfs(amt - coin, dp, amount, coins);
            if (res == -1) {
                continue;
            }
            cur_min = min(cur_min, res + 1);
        }

        dp[amt] = cur_min == amount + 1 ? -1 : cur_min;
        return dp[amt];
    }

    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
    
        return dfs(amount, dp, amount, coins);
    }
};
