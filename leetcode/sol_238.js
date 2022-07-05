//this code runs in O(3n) -> O(n)
// but im still dissapointed cause in memory is also (n)
// and i wanted memory O(1)... gonna search that one

nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
test = nums2

var productExceptSelf = function (nums) {
    let N = Object.keys(nums).length
    const ans1 = new Array(N)
    const ans2 = new Array(N)
    ans1.fill(1)
    ans2.fill(1)
    for (let i = 1; i < nums.length; ++i) {
        ans1[i] = ans1[i-1]*nums[i-1]
    }
    for (let i = nums.length - 2; i>=0; --i) {
        ans2[i] = ans2[i+1]*nums[i+1]
    }
    const ans = new Array(N)
    for (let i = 0; i < nums.length; ++i) {
        ans[i] = ans1[i]*ans2[i]
    }
    return ans
};

const ans = productExceptSelf(test)
ans.forEach((el) => console.log(el))
