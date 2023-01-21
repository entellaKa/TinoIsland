map1 = [[1]*30 for i in range(20)]
MAP1 = """0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,0,0,2,2,2,3
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,3
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
"""
MAP2 = """0	0	0	0	0	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	0	0	2	2	2	2
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	9	9	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	9	9	1	1	1	1	1	1	1	1	1	1	9	9	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	9	9	1	1	1	1	1	1	1	1	1	1	9	9	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	9	9	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	9	9	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	9	9	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	9	9	1	1	1	1	1	9	9	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	9	9	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	9	9	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	9	9	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	9	9	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	9	9	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	1	1	1	1	0	0	1	1	1	3
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	4	4	4	4	4	4	4	4	0	0	4	4	4	3"""


map1 = [list(map(int, MAP1.split('\n')[i].split(','))) for i in range(20)]
map2 = [list(map(int, MAP2.split('\n')[i].split('	'))) for i in range(20)]

maps = [[map1, map2]]



