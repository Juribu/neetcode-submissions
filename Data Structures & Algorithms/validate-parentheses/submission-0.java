class Solution {
    public boolean isValid(String s) {
       // for each char in s
            // if it is a opening bracket, push into stack
            // else if it is closing bracket pop the stack and compare

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '{' || c == '(' || c == '[') stack.push(c);
            else {
                // 4 cases
                if (stack.empty()) return false;
                char top = stack.pop();
                switch (c){
                case '}':
                    if (top != '{') return false;
                    break;
                case ']':
                    if (top != '[') return false;
                    break;
                case ')':
                    if (top != '(') return false;
                    break;
                }
            }
        }

        return stack.empty();


    }
}