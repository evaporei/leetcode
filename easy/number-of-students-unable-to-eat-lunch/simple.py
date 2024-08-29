class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        while sandwiches and sandwiches[0] in students:
            top = sandwiches[0]
            if students[i] == top:
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students.pop(0))
        
        return len(students)
