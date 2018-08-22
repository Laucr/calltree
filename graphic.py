# __author__ = Liu bn
# 2018/8/20


class Graphic:
    def __init__(self, node_list, ltt=None):
        self.node_list = node_list
        self.ltt = ltt
        self._edge_ = []
        self._func_ = []
        self._arrow_ = []

        self.__edge__ = "-"
        self.__edge_angle__ = "++"
        self.__edge_sep__ = " -- "

        self.__func_left__ = "[ "
        self.__func_right__ = " ]"
        self.__func_sep__ = " => "

        self.__block_bound__ = "||"

        self.__arrow__ = chr(8595)
        self.__arrow_conj__ = " "
        self.__arrow_sep__ = "  "

    def add_func(self, func_name):
        width = len(func_name) + len(self.__func_left__ + self.__func_right__)
        edge = self.__edge__ * width
        func = self.__func_left__ + func_name + self.__func_right__
        self._edge_.append(edge)
        self._func_.append(func)

    def join_funcs(self):
        for node in self.node_list:
            self.add_func(node.func_name)
        edge = self.__edge_sep__.join(self._edge_)
        func = self.__func_sep__.join(self._func_)

        _arrow_line = self.add_arrow(len(func))
        _edge_line = self.__edge_angle__ + edge + self.__edge_angle__
        _func_line = self.__block_bound__ + func + self.__block_bound__
        block = [_arrow_line, _edge_line, _func_line, _edge_line]
        return block

    def add_arrow(self, width):
        arrow_pos = int(width / 2)
        if width % 2 == 0:
            arrow_pos -= 1
        arrow = [self.__arrow_conj__] * width
        arrow[arrow_pos] = self.__arrow__
        _arrow_line = self.__arrow_sep__ + "".join(arrow) + self.__arrow_sep__
        return _arrow_line

    @staticmethod
    def join_block(blocks, sep):
        _arrow_line = (" " * len(sep)).join([b[0] for b in blocks])
        _edge_line = sep.join([b[1] for b in blocks])
        _func_line = sep.join([b[2] for b in blocks])
        return [_arrow_line, _edge_line, _func_line, _edge_line]
