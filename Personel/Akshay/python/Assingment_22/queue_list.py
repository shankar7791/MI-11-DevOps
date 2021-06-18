queue = []

queue.append('10')
queue.append('20')
queue.append('30')
queue.append('40')


print("Initial queue List :")
print(queue)

print("\nElements dequeued from queue :")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements :")
print(queue)