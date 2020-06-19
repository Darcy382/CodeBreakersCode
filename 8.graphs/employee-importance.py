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
        employee_lookup = {}
        for employee in employees:
            employee_lookup[employee.id] = employee
        return self._getImportance(employee_lookup, id)


    def _getImportance(self, employees, id):
        importance = employees[id].importance
        for subordinate in employees[id].subordinates:
            importance += self._getImportance(employees, subordinate)
        return importance
