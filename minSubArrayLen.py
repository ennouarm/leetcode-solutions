def minSubArrayLen(nums, target):
    l,total = 0,0
    res = float("inf")
    
    for r in range(len(nums)):
        total +=nums[r]
        while total >= target:
            res = min(r-l+1, res)
            total = total -nums[l]
            l+=1
    return 0 if res == float('inf') else res

if __name__=="__main__":
    print(minSubArrayLen([1,4,4], 4))