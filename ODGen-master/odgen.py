#!/usr/bin/env python3

from src.core.opgen import OPGen
from src.core.graph import Graph
# from src.core.options import parse_args, setup_graph_env
from src.core.options import parse_args


if __name__ == '__main__':
    # args = parse_args()
    opg = OPGen()
    opg.run()
    a=1
    #print(G.op_cnt)

