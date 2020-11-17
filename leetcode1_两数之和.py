class Solution(object):
    '''
       返回和为target的两个数
    '''
    def twoSum01(self, nums, target):
        sorted(list(nums))
        len=len(nums)
        left=0
        right=len-1
        res=[]
        while left<right:
            if(nums[left]+nums[right]>target):
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                res.append([nums[left],nums[right]])
                right -= 1
                left += 1
        return res
    '''
       返回和为target的两个数的索引
    '''
    def twoSum02(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i # nums=[3,3],target=6)
        return []
if __name__ == '__main__':
    print(Solution().twoSum02(nums=[3,3],target=6))
