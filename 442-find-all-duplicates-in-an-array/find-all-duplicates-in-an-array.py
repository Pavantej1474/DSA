class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_set ={}
        ls=[]

        for i in range(0, len(nums)):
            if nums[i] in num_set:
                num_set[nums[i]]=2
            else:
                num_set[nums[i]]=1
        
        for key, val in num_set.items():
            if val ==2:
                ls.append(key)
            
        return ls


        
            

        