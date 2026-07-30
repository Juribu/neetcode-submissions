class Solution {
    public int hammingWeight(int n) {
        // count the number of 1
        // loop through 32 because int is size 32
            // right shift each time and see if it is 1

        int count = 0;
        for (int i = 0; i < 32; i++) {
            count = ((n & (1 << i)) != 0 ) ? ++count : count;
        }

        return count;
    }
}