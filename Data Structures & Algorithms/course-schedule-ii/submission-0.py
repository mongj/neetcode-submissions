class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = defaultdict(list)
        for prereq in prerequisites:
            prereqMap[prereq[0]].append(prereq[1])
        
        visited = set()
        courses_taken = set()
        path = []
        # tries to take the course, recursively completes prereqs if any
        # return False if this is not possible
        def dfs(course_id: int) -> bool:
            if course_id in visited:
                return False
            if course_id in courses_taken:
                return True
            
            visited.add(course_id)
            
            # complete prerequisites
            for p in prereqMap[course_id]:
                if not dfs(p):
                    return False
            
            visited.remove(course_id)

            # prerequisites are completed, now we can take the course
            path.append(course_id)
            courses_taken.add(course_id)
            prereqMap[course_id] = []

            return True
        
        for course_id in range(numCourses):
            if not dfs(course_id):
                return []
        return path