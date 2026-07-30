class Solution {
    public int[] countBits(int n) {
        // loop through 1-n
        // loop through all 32 bits
          // count the ones
        int[] solution = new int[n+1];

        for (int i = 0; i <= n; i++) {
            int count = 0;
            for (int j = 0; j < 32; j++) {
                count = ((i & ( 1 << j)) != 0) ? count + 1 : count;
            }
            solution[i] = count;
        }

        return solution;
    }
}
