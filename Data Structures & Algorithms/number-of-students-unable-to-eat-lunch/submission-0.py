class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0  # tracks consecutive failures

        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0  # reset because someone ate
            else:
                students.append(students.popleft())
                count += 1  # one failed attempt

        return len(students)