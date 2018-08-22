# __author__ = Liu bn
# 2018/8/17


class Node:
    def __init__(self, _node_info):
        self._node_info_ = _node_info
        self.func_name = ""
        self.comment = ""
        self.son_list = []
        self.extract_node_info()

    def extract_node_info(self):
        if not self._node_info_:
            return
        _div = self._node_info_.split("#")
        self.func_name = _div[0].strip()
        if len(_div) > 1:
            self.comment = _div[1:][0].strip()

    def add_son_list(self, sons):
        self.son_list = sons


def get_node(_level, _line):
    _line = _line.strip()
    _node = _line.split(" ")[_level:]
    _node_info = " ".join(_node)
    return _node_info


def store_node_list(_list):
    return list(map(lambda x: x[1], reversed(_list)))


def ltt_add_node(_ltt, level, node):
    if level in _ltt.keys():
        _ltt[level].append(node)
    else:
        _ltt[level] = [node]


def get_tree(_file_name):
    lines = []
    with open(_file_name, 'r', encoding="utf8") as f:
        lines += f.readlines()

    # level traversal tree
    ltt = {}

    stack = []
    for line in lines:
        level = line.count("|")
        node = Node(get_node(level + 1, line))
        ltt_add_node(ltt, level, node)
        if not stack:
            stack.append((level, node))
        else:
            if stack[-1][0] <= level:
                stack.append((level, node))
            else:
                popped = []
                while level < stack[-1][0]:
                    if not popped:
                        popped.append(stack.pop())
                    else:
                        if stack[-1][0] != popped[-1][0]:
                            top = stack.pop()
                            top[1].add_son_list(store_node_list(popped))
                            popped = [top]
                        else:
                            popped.append(stack.pop())
                if popped:
                    stack[-1][1].add_son_list(store_node_list(popped))
                stack.append((level, node))

    popped = []
    while len(stack) > 1:
        if not popped:
            popped.append(stack.pop())
        else:
            if stack[-1][0] != popped[-1][0]:
                top = stack.pop()
                top[1].add_son_list(store_node_list(popped))
                popped = [top]
            else:
                popped.append(stack.pop())
    stack[0][1].add_son_list(store_node_list(popped))

    return ltt
