import heapq


hull, nodes, links = map(int, input().split())

graph = {}
for i in range(links):
    a, b, t, h = map(int, input().split())
    graph[a] = graph.get(a, []) + [(b, t, h)]
    graph[b] = graph.get(b, []) + [(a, t, h)]

start, end = map(int, input().split())

visited = [False] * (nodes + 1)
weights  = [(float('inf'), float('inf'))] * (nodes + 1)
weights[start] = (0, 0) 
queue = [(0, 0, start)]

while len(queue) > 0:
    current = heapq.heappop(queue)[2]
    visited[current] = True

    for link in graph.get(current, []):
        i, t, h = link

        if visited[i]:
            continue

        if weights[i][0] > weights[current][0] + t and hull > weights[current][1] + h:
            weights[i] = (weights[current][0] + t, weights[current][1] + h)
            heapq.heappush(queue, (weights[i][0], weights[i][1], i))


if weights[end][0] == float('inf'):
    print(-1)
else:
    print(weights[end][0])



"""
You are travelling on a ship in an archipelago. The ship has a convex hull which is K centimetres thick. The archipelago has N islands, numbered from 1 to N. There are M sea routes amongst them, where the i-th route runs directly between two different islands ai and bi (1 ≤ ai, bi ≤ N), takes ti minutes to travel along in either direction, and has rocks that wear down the ship's hull by hi centimetres. There may be multiple routes running between a pair of islands.

You would like to travel from island A to a different island B (1 ≤ A, B ≤ N) along a sequence of sea routes, such that your ship's hull remains intact – in other words, such that the sum of the routes' hi values is strictly less than K.

Additionally, you are in a hurry, so you would like to minimize the amount of time necessary to reach island B from island A. It may not be possible to reach island B from island A, however either due to insufficient sea routes or the having the ship's hull wear out.

Input
The first line of input contains three integers K, N and M (1 ≤ K ≤ 200; 2 ≤ N ≤ 2000; 1 ≤ M ≤ 10000), each separated by one space.

The next M lines each contain 4 integers ai bi ti hi (1 ≤ ai, bi ≤ N; 1 ≤ ti ≤ 105; 0 ≤ hi ≤ 200), each separated by one space. The i-th line in this set of M lines describes the i-th sea route (which runs from island ai to island bi, takes ti minutes and wears down the ship's hull by hi centimetres). Notice that ai ≠ bi (that is, the ends of a sea route are distinct islands).

The last line of input contains two integers A and B (1 ≤ A, B ≤ N; A ≠ B), the islands between which we want to travel.

For 20% of marks for this question, K = 1 and N ≤ 200. For another 20% of the marks for this problem, K = 1 and N ≤ 2000.

Output
Output a single integer: the integer representing the minimal time required to travel from A to B without wearing out the ship's hull, or -1 to indicate that there is no way to travel from A to B without wearing out the ship's hull.

Sample Input 1
10 4 7
1 2 4 4
1 3 7 2
3 1 8 1
3 2 2 2
4 2 1 6
3 4 1 1
1 4 6 12
1 4

Sample Output 1
7

Explanation of Sample 1
The path of length 1 from 1 to 4 would wear out the hull of the ship. The three paths of length 2 ([1, 2, 4] and [1, 3, 4] two different ways) take at least 8 minutes. The path [1, 2, 3, 4] takes 7 minutes and only wears down the hull by 7 centimetres, whereas the path [1, 3, 2, 4] takes 13 minutes and wears down the hull by 5 centimetres.

Sample Input 2
3 3 3
1 2 5 1
3 2 8 2
1 3 1 3
1 3

Sample Output 2
-1

Explanation of Sample 2
The direct path [1, 3] wears down the hull to 0, as does the path [1, 2, 3].
"""