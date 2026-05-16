# this is just topological sort
from collections import defaultdict, deque
import heapq

def solve(ids):
    lines = ids.split("\n")
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    nodes = set()

    # construct graph
    for line in lines:
        data = line.split(" ")

        parent = data[1]
        child = data[7]

        graph[parent].append(child)
        in_degree[child] += 1
        
        nodes.add(child)
        nodes.add(parent)    
    
    # for part 2 we have an additional elf helper, but now we need to see 
    # which tasks unlock other tasks

    # start bfs    
    heap = []
    visited = set()
    res = 0

    # init heap
    for node in nodes:
        if node not in in_degree or in_degree[node] == 0:
            heap.append(node)
            visited.add(node)
    
    heapq.heapify(heap)

    running = [["", -1], ["", -1], ["", -1], ["", -1], ["", -1]]
    k = len(running)
    curr_running = 0

    while heap or curr_running > 0:  # every iteration represents a second
        # try to assign as many tasks as possible
        for i in range(k):
            if running[i][0] != "" and running[i][1] != -1:
                continue
            
            if heap:
                curr = heapq.heappop(heap)
                running[i] = [curr, ord(curr) - ord('A') + 1 + 60]
                curr_running += 1
        
        # print(f"After trying to assign all possible tasks, running is: {running}")
        
        # now that we've assigned all tasks possible, we should process them for 1 second
        completed = []
        for i in range(k):
            if running[i][0] == "" and running[i][1] == -1:
                continue
            running[i][1] -= 1

            if running[i][1] == 0:
                completed.append(running[i][0])
                running[i] = ["", -1]
                curr_running -= 1
        
        # print(f"after processing 1 second {running}")
                
        # now add all eligible tasks to heap to be taken by 1 of 5 workers
        for task in completed:         
            # update their children's in-degrees
            for child in graph[task]:
                in_degree[child] -= 1

            # add children to heap
            for child in graph[task]:
                if child not in visited and in_degree[child] == 0:
                    heapq.heappush(heap, child)
                    visited.add(child)
        
        res += 1

    return res

test = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""


ids = """Step B must be finished before step K can begin.
Step F must be finished before step I can begin.
Step T must be finished before step U can begin.
Step R must be finished before step Z can begin.
Step N must be finished before step S can begin.
Step X must be finished before step Y can begin.
Step I must be finished before step Y can begin.
Step K must be finished before step L can begin.
Step U must be finished before step J can begin.
Step G must be finished before step L can begin.
Step W must be finished before step A can begin.
Step H must be finished before step Q can begin.
Step M must be finished before step L can begin.
Step P must be finished before step L can begin.
Step L must be finished before step A can begin.
Step V must be finished before step Y can begin.
Step Q must be finished before step Y can begin.
Step Z must be finished before step J can begin.
Step O must be finished before step D can begin.
Step Y must be finished before step A can begin.
Step J must be finished before step E can begin.
Step A must be finished before step E can begin.
Step C must be finished before step E can begin.
Step D must be finished before step E can begin.
Step S must be finished before step E can begin.
Step B must be finished before step R can begin.
Step U must be finished before step O can begin.
Step X must be finished before step I can begin.
Step C must be finished before step S can begin.
Step O must be finished before step S can begin.
Step J must be finished before step D can begin.
Step O must be finished before step E can begin.
Step Z must be finished before step O can begin.
Step J must be finished before step C can begin.
Step P must be finished before step Y can begin.
Step X must be finished before step S can begin.
Step O must be finished before step Y can begin.
Step J must be finished before step A can begin.
Step H must be finished before step C can begin.
Step P must be finished before step D can begin.
Step Z must be finished before step S can begin.
Step T must be finished before step Z can begin.
Step Y must be finished before step C can begin.
Step X must be finished before step H can begin.
Step R must be finished before step Y can begin.
Step T must be finished before step W can begin.
Step L must be finished before step O can begin.
Step G must be finished before step Z can begin.
Step H must be finished before step P can begin.
Step I must be finished before step U can begin.
Step H must be finished before step V can begin.
Step N must be finished before step Y can begin.
Step Q must be finished before step E can begin.
Step H must be finished before step D can begin.
Step P must be finished before step O can begin.
Step T must be finished before step I can begin.
Step W must be finished before step V can begin.
Step K must be finished before step M can begin.
Step R must be finished before step W can begin.
Step B must be finished before step T can begin.
Step U must be finished before step A can begin.
Step N must be finished before step H can begin.
Step F must be finished before step U can begin.
Step Q must be finished before step O can begin.
Step Y must be finished before step S can begin.
Step V must be finished before step O can begin.
Step W must be finished before step C can begin.
Step Y must be finished before step J can begin.
Step T must be finished before step V can begin.
Step N must be finished before step D can begin.
Step U must be finished before step Q can begin.
Step A must be finished before step C can begin.
Step U must be finished before step M can begin.
Step Q must be finished before step S can begin.
Step P must be finished before step V can begin.
Step B must be finished before step Z can begin.
Step W must be finished before step Q can begin.
Step L must be finished before step S can begin.
Step I must be finished before step P can begin.
Step G must be finished before step P can begin.
Step L must be finished before step C can begin.
Step K must be finished before step A can begin.
Step D must be finished before step S can begin.
Step I must be finished before step H can begin.
Step R must be finished before step M can begin.
Step Q must be finished before step D can begin.
Step K must be finished before step O can begin.
Step I must be finished before step C can begin.
Step N must be finished before step O can begin.
Step R must be finished before step X can begin.
Step P must be finished before step C can begin.
Step B must be finished before step Y can begin.
Step G must be finished before step E can begin.
Step L must be finished before step V can begin.
Step W must be finished before step Y can begin.
Step C must be finished before step D can begin.
Step M must be finished before step J can begin.
Step F must be finished before step N can begin.
Step T must be finished before step Q can begin.
Step I must be finished before step E can begin.
Step A must be finished before step D can begin."""


print(solve(ids))