import collections
def solution(participant, completion):
    countP = collections.Counter(participant)
    countC = collections.Counter(completion)
    res = countP - countC
    return list(res.keys())[0]


a = ["mislav", "stanko", "mislav", "ana"];
b = ["stanko", "ana", "mislav"];
print(solution(a, b))