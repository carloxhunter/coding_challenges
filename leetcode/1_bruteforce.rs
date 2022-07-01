//this solution is simple brutefoce, i'd rather get a less than O(n^2) algorithm
//but havent thought about it yet. Works

struct Solution();

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut vec: Vec<i32> = Vec::new();
        let mut c = 0;
        for (pos1, e1) in nums.iter().enumerate() {
            for (pos2, e2) in nums.iter().enumerate() {
                if e1 + e2 == target && pos2 != pos1 {
                    vec.push(c);
                }
            }
            c += 1
        }
        return vec;
    }
}

fn main() {
    println!("Hello World");
    let vec: Vec<i32> = vec![0, 4, 3, 0];
    let target = 0;
    let sol = Solution::two_sum(vec, target);
    println!("{:?}", sol)
}
