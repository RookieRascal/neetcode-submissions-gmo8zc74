class Solution {
    public int[] twoSum(int[] nums, int target) {
      Map <Integer,Integer> m = new HashMap<>();
     int a;
     for(int i = 0; i<nums.length; i++){
      a = target-nums[i];
      if(m.containsKey(a)){
        return new int [] {m.get(a), i};
      }
      m.put(nums[i], i);
     }
     return new int [] {};
    }
}
