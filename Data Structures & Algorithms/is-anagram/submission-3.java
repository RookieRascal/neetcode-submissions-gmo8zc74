class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
    HashMap <Character, Integer> c = new HashMap<>();
    HashMap <Character, Integer> r = new HashMap<>();
    for(int i = 0; i<s.length(); i++){
        c.put(s.charAt(i), c.getOrDefault(s.charAt(i), 0)+1);
        r.put(t.charAt(i), r.getOrDefault(t.charAt(i), 0)+1);
        
       }
       return c.equals(r);
    }
}
