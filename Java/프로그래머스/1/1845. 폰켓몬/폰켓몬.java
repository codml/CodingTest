import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap <Integer, Integer> map = new HashMap <>();
        
        for (int n: nums)
            map.put(n, map.getOrDefault(n, 0) + 1);
        
        int size = map.size();
        if (size > nums.length / 2)
            answer = nums.length / 2;
        else
            answer = size;
        
        return answer;
    }
}