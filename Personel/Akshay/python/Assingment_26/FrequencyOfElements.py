from collections import Counter
from itertools import chain
nums = [
        [1,2,3,2],
        [4,5,6,2],
        [7,1,9,5],
]

print("Original list of lists:")
print(nums)
print("\nFrequncy of the elements in the said list of lists:")
result = Counter(chain.from_iterable(nums))
print(result)