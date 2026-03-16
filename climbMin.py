
def climbMin(array :list[int])->int:
    n = len(array)
    prev1 = array[1]
    prev2 = array[0]
    for i in range(2,n):
        current = min(prev1,prev2)+ array[i]
        prev2=prev1
        prev1=current
    return min(prev1,prev2)
    
    
if __name__==__name__:
    n =[5,18,4,15,6]
    res = climbMin(n)
    print(res)
