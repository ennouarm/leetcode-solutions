from heapq import heapify, heappop

def find_kth_largest(nums: list[int], k: int) -> int:
    nums = [-x for x in nums]
    heapify(nums)
    for _ in range(k-1):
        heappop(nums)
    return -nums[0]

if __name__=="__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    res = find_kth_largest(nums,k)
    print(res)