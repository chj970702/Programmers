def solution(n, wires):

    def dfs(a):
        visited[a] = 1  # 방문표시
        for k in range(1, n + 1):
            if not visited[k] and check[a][k] == 1:
                dfs(k)

    answer = []

    for i in range(len(wires)):
        check = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(len(wires)):
            check[wires[j][0]][wires[j][1]] = 1
            check[wires[j][1]][wires[j][0]] = 1
        visited = [0] * (n + 1)
        check[wires[i][0]][wires[i][1]] = 0
        check[wires[i][1]][wires[i][0]] = 0
        dfs(wires[i][0])
        check1 = sum(visited)
        visited = [0] * (n + 1)
        dfs(wires[i][1])
        check2 = sum(visited)
        answer.append(abs(check1 - check2))
    return min(answer)

# print(solution(9, [[1,3], [2,3], [3,4], [4,5], [4,6], [4,7], [7,8], [7,9]]))
# print(solution(4, [[1,2],[2,3],[3,4]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))