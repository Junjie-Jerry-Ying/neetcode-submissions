
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> sSeen = new HashMap<>();
        Map<Character, Integer> tSeen = new HashMap<>();
        for (int i=0; i<s.length(); i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            sSeen.put(sChar, sSeen.getOrDefault(sChar, 0)+1);
            tSeen.put(tChar, tSeen.getOrDefault(tChar, 0)+1);
        }
        return sSeen.equals(tSeen);
    }
}
