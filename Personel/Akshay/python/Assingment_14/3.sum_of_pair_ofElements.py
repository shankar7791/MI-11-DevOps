class Num:
       def twoSum(self, nums, target):
        val = {}
        for i, num in enumerate(nums):
            if target - num in val:
                return (val[target - num], i )
            val[num] = i

call = Num()
int1, int2 = call.twoSum([10,20,10,40,50,60,70],50)
print(int1 + 1 , int2 + 1)