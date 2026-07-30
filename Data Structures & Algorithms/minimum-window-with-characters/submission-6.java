class Solution {
    public String minWindow(String s, String t) {
        if (t.length() == 0 || s.length() == 0) return "";

        // Frequency maps
        Map<Character, Integer> targetFreq = new HashMap<>();
        Map<Character, Integer> windowFreq = new HashMap<>();

        // Build frequency map for t
        for (char c : t.toCharArray()) {
            targetFreq.put(c, targetFreq.getOrDefault(c, 0) + 1);
        }

        int requiredMatches = targetFreq.size();
        int formedMatches = 0;

        int left = 0, right = 0;
        int minStart = 0, minLength = Integer.MAX_VALUE;

        while (right < s.length()) {
            char c = s.charAt(right);
            windowFreq.put(c, windowFreq.getOrDefault(c, 0) + 1);

            // If this char satisfies frequency condition
            if (targetFreq.containsKey(c) && 
                windowFreq.get(c).intValue() == targetFreq.get(c).intValue()) {
                formedMatches++;
            }

            // Try to shrink from left
            while (left <= right && formedMatches == requiredMatches) {
                int windowLength = right - left + 1;
                if (windowLength < minLength) {
                    minLength = windowLength;
                    minStart = left;
                }

                char leftChar = s.charAt(left);
                windowFreq.put(leftChar, windowFreq.get(leftChar) - 1);

                if (targetFreq.containsKey(leftChar) && 
                    windowFreq.get(leftChar) < targetFreq.get(leftChar)) {
                    formedMatches--;
                }
                left++;
            }

            right++;
        }

        return minLength == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLength);
    }
}
