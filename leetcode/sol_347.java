package leetcode;

import java.util.HashMap;

public class sol_347 {
    public static void main(String args[]) {
        Solution sol = new Solution();
        int input[] = { 1, 1, 1, 2, 2, 3 };
        int kval = 2;
        sol.topKFrequent(input, kval);
    }
}

class Solution {
    void printvals(HashMap<Integer, int[]> HT, int min_of_max, int[] ans) {
        HT.entrySet().forEach(entry->    {
            System.out.println(entry.getKey() + " : [" + entry.getValue()[0] + ", " + entry.getValue()[1] + "]");
        });
        System.out.println("min "+min_of_max);
        System.out.println("arr ans");
        for(int i = 0;i<ans.length;i++)
        {
            System.out.println("ans[" + i + "]:" + ans[i]);
        }
    }
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, int[]> HT = new HashMap<Integer, int[]>();
        boolean isk;
        int min_of_max = nums[0];
        int[] ans = new int[k];
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            isk = HT.containsKey(val);
            boolean st = i + 1 <= k;
            //System.out.println(starting+" "+k);
            if (!isk && st) {   
                HT.put(val, new int[] { 1, i });
                ans[i] = val;
                //keep track of min_of_max
                if (1 <= HT.get(min_of_max)[0]){
                    min_of_max = val;
                } 
            }
            else if(!isk && !st){
                HT.put(val, new int[] { 1, -1 });
            }
            else {
                int[] vals = HT.get(val);
                int[] mins = HT.get(min_of_max);
                vals[0]+=1;

                if (vals[0] <= HT.get(min_of_max)[0]){
                    int idx = mins[1];
                    System.out.println("idx "+idx+" vals {"+vals[0]+" : "+vals[1]+"}");
                    ans[idx]=vals[0];
                    //min_of_max = vals[1];
                } 

            }
        }


    printvals(HT, min_of_max, ans);
    int intArray[] = { 13, 14, 15 };
    return intArray;
}}
