def solution(tickets):
    routes = {}
    visited = {}
    
    for ticket in tickets:
        for airport in ticket:
            if airport not in routes:
                routes[airport] = []
                visited[airport] = {}
        
        arr = ticket[0]
        dep = ticket[1]
        routes[arr].append(dep)
        if dep in visited[arr]:
            visited[arr][dep] += 1
        else:
            visited[arr][dep] = 1
        routes[arr].sort()

    def dfs(cur, answer):
        if len(answer) - 1 == len(tickets):
            return answer

        for next_ in routes[cur]:
            if visited[cur][next_] > 0:
                visited[cur][next_] -= 1
                result = dfs(next_, answer + [next_])
                visited[cur][next_] += 1
                if result:
                    return result
        return None

    answer = dfs('ICN', ['ICN'])
    
    return answer