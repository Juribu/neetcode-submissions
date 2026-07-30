class Solution {
    public boolean isAnagram(String s, String t) {
        // make an array for all chars
        // loop over length of s, add to array[c] if in s, and minus if in t
        if (s.length() != t.length()) return false;
        int[] chars = new int[26];

        for (int i = 0; i < s.length(); i++) {
            chars[s.charAt(i) - 'a']++;
            chars[t.charAt(i) - 'a']--;
        }
        // check if array == 0
        for (int c : chars) {
            if (c != 0) return false;
        }

        return true;
    }
}