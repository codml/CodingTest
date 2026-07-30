answer = 0

def solution(n):
    
    chess = [0 for _ in range(n)]
    
    def is_possible(cur, col):
        for i in range(cur):
            if chess[i] == col or chess[i] - col == i - cur or chess[i] - col == cur - i:
                return False
        return True
    
    def backtrack(cur):
        if cur == n:
            global answer
            answer += 1
        
        for i in range(n):
            if is_possible(cur, i):
                chess[cur] = i
                backtrack(cur + 1)
    backtrack(0)
    return answer