

def getSum(nums, target):
    visitedSet = set()
    for num in nums:
        if target-num in visitedSet:
            return[num, target-num]
        else:
            visitedSet.add(num)
        
    return[-1]
print(getSum([2,7,11,15],17))