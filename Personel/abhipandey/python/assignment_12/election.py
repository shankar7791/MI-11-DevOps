a = ["tony", "steve", "banner", 
      "steve", "tony", "tony", 
      "banner", "tony", "banner",
      "steve", "tony", "steve",
      "banner", "tony" , "banner"]

cand = set(a)
print("Election List -",a)
for cand in set(a):
    print(cand, a.count(cand))

import collections
c = collections.Counter(a)

print(c)
print("Winner -",c.most_common(1)) 