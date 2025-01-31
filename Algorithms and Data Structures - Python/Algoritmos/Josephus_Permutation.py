from collections import deque
def solution(array, k):
    d = deque(array)
    permutation = []
    while d:
        d.rotate(1-k)
        item = d.popleft()
        permutation.append(item)
    return permutation

soldiers = 7
arr = [s+1 for s in range(soldiers)]
k = 3
perm = solution(arr, k)
print(perm)