def two_sum(nums, target):
    seen = {}  
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[num] = i
arr = [3, 8, 9, 10, 25]
tar = 19
print(two_sum(arr, tar))