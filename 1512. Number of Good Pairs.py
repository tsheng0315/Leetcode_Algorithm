'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:
'''

# My solution:
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count =0
        nums_length=len(nums)
        for i in range(nums_length):
            for j in range(i+1,nums_length):
                if nums[i]=nums[j]:
                    count+=1
        return count
 

#Dom: dict+ pointer; key->number, value->frequency
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_by_number={}
        for n in nums:
            if n not in count_by_number:# n appeared for the first time
                count_by_number[n]=1
            else:
                count_by_number[n]+=1
        result=0
        value=count_by_number.values()
        for v in value:
            result+=v*(v-1)//2
        return result

# online

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(v * (v - 1) // 2 for v in collections.Counter(nums).values())  # dict.values()  return value
    
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        return sum(v * (v - 1) // 2 for key,v in collections.Counter(nums).items())  # dict.items() return key and value 
    



