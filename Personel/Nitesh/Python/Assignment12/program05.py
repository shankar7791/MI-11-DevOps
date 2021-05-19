
e = ["raj", "rohit", "rahul", 
      "sumit", "rahul", "sumit", 
      "raj", "sumit", "rahul",
      "sumit", "rahul", "rahul",
      "raj", "rohit"]

cand = set(e)
print("Election List -",e)
for cand in set(e):
    print(cand, e.count(cand))

import collections
c = collections.Counter(e)

print(c)
print("Winner -",c.most_common(1))