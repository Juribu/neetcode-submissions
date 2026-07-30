class Solution {
    public boolean isPalindrome(String s) {

        s = s.toLowerCase().replaceAll("[^0-9a-zA-Z]", "");
        if (s.length() == 0) return true;
        s = s.toLowerCase();

        // two pointers left and right
        // close the window and check char at each edge
        int left = 0, right = s.length() -1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++; right--;
        }

        return true;
    }
}