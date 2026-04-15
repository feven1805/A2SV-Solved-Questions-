class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        res = []
        visited = set()
        q = deque([s])
        visited.add(s)
        found = False
        
        while q:
            curr = q.popleft()
            
            if is_valid(curr):
                res.append(curr)
                found = True
            
            if found:
                continue  
            
            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                
                nxt = curr[:i] + curr[i+1:]
                
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        
        return res if res else [""]