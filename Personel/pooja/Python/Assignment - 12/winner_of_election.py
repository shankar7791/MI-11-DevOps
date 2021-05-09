a = ["john", "johnny", "harry", 
      "harry", "john", "jackie", 
      "jamie", "jamie", "harry",
      "johnny", "harry", "johnny",
      "harry", "john"]

cand = set(a)
print("Election List -",a)
for cand in set(a):
    print(cand, a.count(cand))

import collections
c = collections.Counter(a)

print(c)
print("Winner -",c.most_common(1))