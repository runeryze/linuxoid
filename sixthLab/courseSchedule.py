from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_matrix = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_matrix[prereq].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        visited_courses = 0

        while queue:
            current_course = queue.popleft()
            visited_courses += 1

            for next_course in adj_matrix[current_course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return visited_courses == numCourses
