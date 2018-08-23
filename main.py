# __author__ = Liu bn
# 2018/8/20

import make_tree as mt
from graphic import Graphic

ltt = mt.get_tree("call.txt")
graph = {0: Graphic(ltt[1]).join_funcs()}

depth = sorted(ltt.keys())[-1]
i = 1

width = len(graph[0][2])
logic_path = {
    0: lambda x, y: x[0],
    1: Graphic.join_block,
}
sep = "   "
while i <= depth:
    gr_list = []
    for n in ltt[i]:
        if n.son_list:
            gr_list.append(Graphic(n.son_list).join_funcs())
    if gr_list:
        w = logic_path[0 if len(gr_list) == 0 else 1](gr_list, sep)
        graph[i] = w
        if width < len(w[0]):
            width = len(w[0])
    print(width)
    i += 1

for k in graph:
    print("\n".join(graph[k]))
