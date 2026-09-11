class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(list)
        for p in prerequisites:
            prereqMap[p[0]].append(p[1])
        
        visited = set()
        def hasCycle(course_id: int) -> bool:
            if course_id in visited:
                return True
            visited.add(course_id)

            for prereq in prereqMap[course_id]:
                if hasCycle(prereq):
                    return True

            visited.remove(course_id)
            prereqMap[course_id] = []
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True