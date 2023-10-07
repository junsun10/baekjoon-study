# 내리막 길 ( 시간초과 )
# bfs 시간초과

from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((0, 0))

while dq:
    x, y = dq.popleft()

    if x == m-1 and y == n-1:
        answer += 1
        continue

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if (0 <= nx < m) and (0 <= ny < n) and arr[x][y] > arr[nx][ny]:
            dq.append((nx, ny))

print(answer)
