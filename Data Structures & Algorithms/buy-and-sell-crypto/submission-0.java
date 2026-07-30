class Solution {
    public int maxProfit(int[] prices) {
        // keep track of minimum price
        // keep track of maximum profit
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        // loop through all the prices
        // if the price is lower than min price, then update min price
        // if the price is not loewr than min price, then see if the diff is greater than max profit
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) minPrice = prices[i];
            else if ((prices[i] - minPrice) > maxProfit) maxProfit = prices[i] - minPrice;
        }
        return maxProfit;
    }
}