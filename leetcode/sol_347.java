package leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class sol_347 {
    public static void main(String args[]) {
        Solution sol = new Solution();
        int input[] = { 1, 1, 1, 2, 2, 3 };
        int input2[] = { 4, 1, -1, 2, -1, 2, 3 };
        int kval = 2;
        sol.topKFrequent(input2, kval);
    }
}

class Solution {
    void printvals(LinkedHashMap<Integer, Integer> HT, int min_of_max, int[] ans) {
        HT.entrySet().forEach(entry -> {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        });
        System.out.println("min " + min_of_max);
        System.out.println("arr ans");
        for (int i = 0; i < ans.length; i++) {
            System.out.println("ans[" + i + "]:" + ans[i]);
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        if (nums.length == 1) {
            return nums;
        }
        LinkedHashMap<Integer, Integer> HT = new LinkedHashMap<Integer, Integer>();
        boolean isk;
        int[] ans = new int[k];
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            isk = HT.containsKey(val);
            if (!isk) {
                HT.put(val, 1);
            } else {
                int rval = HT.get(val);
                HT.put(val, rval + 1);
            }
        };
        List<Map.Entry<Integer, Integer>> list = new ArrayList<Map.Entry<Integer, Integer>>(HT.entrySet());
        Collections.sort(
                list,
                new Comparator<Map.Entry<Integer, Integer>>() {
                    // Comparing two entries by value
                    public int compare(
                            Map.Entry<Integer, Integer> entry1,
                            Map.Entry<Integer, Integer> entry2) {

                        // Substracting the entries
                        return entry1.getValue()
                                - entry2.getValue();
                    }
                });
        int cc = 0;
        int lsize = list.size();
        boolean valid = false;
        int arridx = 0;
        for (Map.Entry<Integer, Integer> vals : list) {
            valid = lsize - cc <= k;
            arridx = lsize-cc-1;
            if (valid){
                ans[arridx] = vals.getKey();
            }
            
            cc+=1;
        }
        return ans;
    }
}
