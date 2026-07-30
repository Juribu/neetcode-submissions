class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            int[] chars = new int[26];

            for (char c : s.toCharArray()) {
                chars[c - 'a']++;
            }
            String sortedString = Arrays.toString(chars);

            // check the hashmap
            // if it is in the hashmap, append s into the map.get(sortedString)
            // else make a new list and append s into new list then add the list into the hasmap
            if (map.get(sortedString) != null) {
                map.get(sortedString).add(s);
            } else {
                List<String> newList = new ArrayList<>();
                newList.add(s);
                map.put(sortedString, newList);
            }
        }

        return new ArrayList<>(map.values());
    }
}