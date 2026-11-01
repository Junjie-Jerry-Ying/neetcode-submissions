
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> anaMap = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            String currString = strs[i];

            List<Integer> anaKey =
                new ArrayList<>(Collections.nCopies(26, 0));

            for (int j = 0; j < currString.length(); j++) {
                char currChar = currString.charAt(j);
                int index = currChar - 'a';

                anaKey.set(index, anaKey.get(index) + 1);
            }

            if (!anaMap.containsKey(anaKey)) {
                anaMap.put(anaKey, new ArrayList<>());
            }

            anaMap.get(anaKey).add(currString);
        }

        return new ArrayList<>(anaMap.values());
    }
}
