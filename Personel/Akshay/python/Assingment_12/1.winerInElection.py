# Prongram for Winner in election
a = ["akii", "rahul", "rahul",  "akii", "rahul", "akii", 
      "rahul", "akii", "rahul", "rahul", "akii", "rahul"]

sim = set(a)
print("Election List -",a)
for sim in set(a):
    print(sim, a.count(sim))

import collections
c = collections.Counter(a)
print(c)
print("Winner -",c.most_common(1))