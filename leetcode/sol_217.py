class Solution(object):
    def containsDuplicate(self, nums):
        #being honest i thought this was slow and didnt apply at begin
        #also thought about set version, but i rather using more agnostic languaje               #solution
        L = len(nums)
        if L == 1: return False
        if L < 1 or L > 100000:
            return False 
        nums.sort()
        n=None
        for z in nums:
            if z == n: return True
            n=z
        return False

file = open('very_large_list.txt','r')
lines_list = []
for line in file:
  lines_list.extend([ int(z) for z in line.split(',')])


t1 = [1,2,1,4]
S=Solution()
sol = S.containsDuplicate(lines_list)
print(sol)





