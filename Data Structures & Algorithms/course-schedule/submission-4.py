class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(list)
        for p in prerequisites:
            prereqMap[p[0]].append(p[1])
        
        visited = set()
        def hasCycle(course_id: int, path: dict) -> bool:
            if course_id in path:
                return True
            if course_id in visited:
                return False
            path[course_id] = "dummy"
            visited.add(course_id)

            for prereq in prereqMap[course_id]:
                if hasCycle(prereq, path):
                    return True

            path.pop(course_id)
            return False
        
        path = {}
        for course in list(prereqMap.keys()):
            if hasCycle(course, path):
                return False
        return True