from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_list(nums):
    return reduce(lcm, nums)

print(lcm_list(range(1, 21)))