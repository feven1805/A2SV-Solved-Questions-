"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = {}
        
        for emp in employees:
            mapp[emp.id] = emp
        
        def dfs(emp_id):
            employee = mapp[emp_id]
            total = employee.importance
            
            for subid in employee.subordinates:
                total += dfs(subid)
            
            return total
        
        return dfs(id)