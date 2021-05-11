dicts = {"Harshal" : 0,"WyZo0" : 0}
for i in range(11) :
    print("""
    Select Your Candidate for Voting.
    1.Harshal
    2.WyZo0""")
    cho = int(input())
    if cho == 1 :
        count = dicts.get("Harshal")
        count += 1
        dicts["Harshal"] = count 
    elif cho == 2 :
        count = dicts.get("WyZo0")
        count += 1
        dicts["WyZo0"] = count
if dicts["Harshal"] > dicts["WyZo0"] :
    print("Winner of the election is Harshal")
else:
    print("Winner of the election is WyZo0")

