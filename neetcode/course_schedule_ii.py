"""
https://neetcode.io/problems/course-schedule-ii

create a parents dict where we have parent: children
create a child dict where we have child: parents --> replace this with just # of parents, and subtract off as necessary
populate both dicts from prerequisites

create empty list for the course order
Iterate through child dict and find all the children without parents and create list of nodes w/o parents
while list is not empty, pop off a node, add to course_order, find the children with parent dict
remove the node from the parent list in the children dict, if a child has no more parents add to list of nodes w/o parents

if len(course order) == numCourses, return course order, otherwise return empty array

time complexity, len(prereqs) for creating the initial dicts, finding initial children O(numCourses), go through nodes and delete each edge 1 time, O(len(prereq) + numCourses)
space O(len(prereq) + numCourses): # of keys is # of courses, and the total of the vals is number of edges/prereqs

"""

from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list) # parent: [children]
        num_parents_vec = [0]*numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            num_parents_vec[course] += 1
        
        no_parent_nodes = []
        for child, num_parents in enumerate(num_parents_vec):
            if num_parents == 0:
                no_parent_nodes.append(child)
        
        course_order = []
        while no_parent_nodes:
            curr = no_parent_nodes.pop()
            course_order.append(curr)
            for child in adj[curr]:
                num_parents_vec[child] -= 1
                if num_parents_vec[child] == 0:
                    no_parent_nodes.append(child)
        
        if len(course_order) < numCourses:
            return []
        else:
            return course_order


if __name__ == "__main__":
    solution = Solution()

    numCourses = 3; prerequisites = [[1,0]]
    print(solution.findOrder(numCourses, prerequisites))

    numCourses = 3; prerequisites = [[0,1],[1,2],[2,0]]
    assert solution.findOrder(numCourses, prerequisites) == []
