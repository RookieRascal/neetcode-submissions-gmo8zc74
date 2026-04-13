class Solution {
    public boolean isAnagram(String s, String t) {
if(s.length()==t.length()){
                for(int i = 0; i < s.length(); i++){
                                if(!t.contains((""+s.charAt(i)))){                
                                                    return false;
                                                                    }
                                                                                    t = t.replaceFirst(""+s.charAt(i),"");
                                                                                                }
                                                                                                            return true;
                                                                                                                    }   
                                                                                                                            return false;     
                                                                                                                               

}
    }

