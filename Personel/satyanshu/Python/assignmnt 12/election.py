from collections import Counter
def winner(input):
	votes=Counter(input)
	dict={}
	for value in votes.values():
		dict[value]=[]
	for (key,value) in votes.items():
		dict[value].append(key)
	maxVote=sorted(dict.keys(),reverse=True)[0]
	if len(dict[maxVote])>1:
		print (sorted(dict[maxvote])[0])
	else:
		print (dict[maxvote][0])
input=['ashwini','ashwini','ashwini','ashwini','dhoni','abd','dhoni','modi','didi','modi','pappu','piggy','yoni']					
winner(input)
