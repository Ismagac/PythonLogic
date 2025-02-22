from typing import List

def binary (self, nums: List[str]) -> List[str]:
    n = len(nums)
    numset = set(nums)

    for index in range(n + 1): #0(n) time complexity, could go up to 2^n
        x = format(index, f'0{n}b')

        if x not in numset and len(x) == n:
            return x
        

print(binary(3, ["010", "101", "111"])) # 000
