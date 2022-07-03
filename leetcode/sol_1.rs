/* this solution works on O(n) as expected in challenge
without brute force */


struct Solution();

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut vec: Vec<i32> = Vec::new();
        let mut diffmap: HashMap<i32, i32> = HashMap::new();
        let mut c = 0;
        let mut helper: i32;
        for i in nums {
            let i: i32 = i;
            if !diffmap.contains_key(&(i)) {
                diffmap.insert(target - i, c);
            } else {
                helper = *diffmap.get(&(i)).unwrap();
                vec.push(c);
                vec.push(helper);
            }
            c += 1
        }
        return vec;
    }
}

fn main() {
    println!("Hello World");
    let vec: Vec<i32> = vec![2, 7, 11, 15];
    let target = 9;
    let sol = Solution::two_sum(vec, target);
    println!("{:?}", sol)
}

