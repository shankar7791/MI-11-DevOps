def same(col, pat):
    if len(col) != len(pat):
        return False
    sdict = {}
    pset = set()
    sset = set()
    for i in range(len(pat)):
        pset.add(pat[i])
        sset.add(col[i])
        if pat[i] not in sdict.keys():
            sdict[pat[i]] = []

        keys = sdict[pat[i]]
        keys.append(col[i])
        sdict[pat[i]] = keys

    if len(pset) != len(sset):
        return False
    
    for val in sdict.values():
        for i in range(len(val) - 1):
            if val[i] != val[i+1]:
                return False

    return True

print("(color1,pat) = "),print(same(["red","green","green"],["a","b","b"]))
print("(strings,color2) = "),print(same(["red","green","greennn"],["a","b","b"]))