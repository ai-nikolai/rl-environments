####################################################
#
# This Work is written by Nikolai Rozanov <nikolai>
#
# Contact:  nikolai.rozanov@gmail.com
#
# Copyright (C) 2018-Present Nikolai Rozanov
#
####################################################

####################################################
# IMPORT STATEMENTS
####################################################

# >>>>>>  Native Imports  <<<<<<<



# >>>>>>  Package Imports <<<<<<<
import unittest
import networkx as nx

# >>>>>>  Local Imports   <<<<<<<
from rlenvs.utils import tree_utils

####################################################
# CODE
####################################################
class MathsUtilsTest(unittest.TestCase):
    """ Basic Tests for maths utils. """
    def test_generation_of_balanced_tree(self):
        BRANCHING_NUMBER = 2
        DEPTH = 3

        graph, root, branching_names = tree_utils.generate_balanced_tree( branching=BRANCHING_NUMBER, depth=DEPTH, return_all=True )

        successors = list( graph.successors(root) )
        number_of_successors = len(successors)

        depth_of_tree = nx.dag_longest_path_length(graph)

        self.assertEqual(number_of_successors,BRANCHING_NUMBER)
        self.assertEqual(depth_of_tree, DEPTH)
        self.assertEqual(root, tree_utils.get_root_name(DEPTH))
        self.assertEqual(len(branching_names), BRANCHING_NUMBER)


    def test_depth_of_node(self):
        BRANCHING_NUMBER = 2
        DEPTH = 3

        graph, root, branching_names = tree_utils.generate_balanced_tree( branching=BRANCHING_NUMBER, depth=DEPTH, return_all=True )

        depth_of_root = tree_utils.get_tree_depth_from_node(root)
        child = list(graph.successors(root))[0]
        depth_of_child = tree_utils.get_tree_depth_from_node(child)

        self.assertEqual(depth_of_root,0)
        self.assertEqual(depth_of_child,1)


####################################################
# MAIN
####################################################
if __name__=="__main__":
    graph, root, action_names = tree_utils.generate_balanced_tree(2,3, return_all=True)
    # tree_utils.print_edges(graph)
    tree_utils.draw_tree(graph)

    for x in graph.successors(root):
        print(x)

    # tree_utils.print_tree_from_root(graph, root)
    # graph = nx.convert_node_labels_to_integers(graph)
    # tree_utils.print_tree_from_root(graph, 0)
    # print(graph.successors(root))
    # print(graph[root][child])




# EOF
