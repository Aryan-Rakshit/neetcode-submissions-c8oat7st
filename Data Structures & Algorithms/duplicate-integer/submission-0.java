class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hSet = new HashSet<>();

        for (int n: nums) {
            if (hSet.contains(n)) {
                return true;
            }

            hSet.add(n);
        }
        
        return false;
    }
}