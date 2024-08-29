class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for sandwich in sandwiches:
            if counter[sandwich] == 0:
                return counter[sandwich ^ 1]
            
            counter[sandwich] -= 1
        return 0
