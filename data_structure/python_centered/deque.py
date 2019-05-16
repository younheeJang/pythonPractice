import collections

DoubleEnded = collections.deque()

DoubleEnded.append("curious")
DoubleEnded.append("jeager")
DoubleEnded.append("queue double ended")
print(DoubleEnded)

DoubleEnded.appendleft("hello")
print(DoubleEnded)

DoubleEnded.pop()
print(DoubleEnded)

DoubleEnded.popleft()
print(DoubleEnded)