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
from typing import Optional, Any


# >>>>>>  Package Imports <<<<<<<
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph, view_pygraphviz


# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################
ROOT_NAME = "ROOT"
def generate_balanced_tree(branching, depth, return_all=False):
    """ Returns a DirectedGraph that is a balanced Tree and the root of the tree. (From left to right)
    branching = 2, depth = 2
    Depth 0 : "ROOT"
    Depth 1 : "!#_B0_" "!#_B1_"
    Depth 2 : "B0_B0_" "B1_B0_" "B0_B1_" "B1_B1_"
    """
    total_size = branching**depth-1
    alphabet = Alphabet(branching)

    graph = nx.DiGraph()

    root = ROOT_NAME
    graph.add_node(root) #root

    _generate_balanced_tree(graph, alphabet, root, 0, branching, depth)

    if return_all:
        return graph, root, alphabet.alphabet
    else:
        return graph


def _generate_balanced_tree(graph, alphabet, current_root, current_depth, branching, total_depth):
    """ recursive graph construction.
    current_root = "!#_!#_B0_"
    current_depth = 1
    total_depth = 3

    ==> always generating for depth+1
    """
    if current_depth<total_depth:
        null_characters_this_turn = total_depth - current_depth
        current_prefix = alphabet.get_null_character() * (null_characters_this_turn-1)
        current_suffix = current_root[ null_characters_this_turn * alphabet.get_null_character_size():]
        for branches_idx in range(branching):
            current_choice = alphabet.get_letter_for_action_index(branches_idx)
            current_node_name = current_prefix + current_choice + current_suffix
            edgelabel_param = Edgelabel.get_param_dict(current_choice)
            graph.add_edge(current_root,current_node_name, **edgelabel_param )
            _generate_balanced_tree(graph, alphabet, current_node_name, current_depth+1, branching, total_depth)


def get_tree_depth_from_node(node):
    """ Returns the depth of the node. """
    if node==ROOT_NAME:
        return 0
    tokens_separated = node.split(Alphabet.get_separator())
    total_depth = len(tokens_separated)-1
    node_height = tokens_separated.count(Alphabet.get_null_character_without_separator())
    return total_depth - node_height
    

def print_tree_from_root(graph, root):
    """
    PRINTS:
    Depth 0 : "!#_!#_B0_"
    Depth 1 : "!#_B0_B0_" "!#_B1_B0_"
    Depth 2 : "B0_B0_B0_" "B1_B0_B0_" "B0_B1_B0_" "B1_B1_B0_"
    """
    print(f"Depth{0}\t:\t{set([root])}")

    current_depth = 1
    current_nodes = set(graph.successors(root))
    while current_nodes:
        print(f"Depth{current_depth}\t:\t{current_nodes}")
        new_current_nodes = set()
        for node in current_nodes:
            new_current_nodes |= set(graph.successors(node))
        current_nodes = new_current_nodes
        current_depth += 1


def print_edges(graph):
    """
    PRINTS:
    ??
    """
    print(graph.edges(data=Edgelabel.get_label_name()))


def draw_tree(graph):
    """ Draws the tree. """
    tmp_path = "tmp.png"
    A = to_agraph(graph)
    # A.write("tmp.txt") #generates a dot readable file
    A.draw(path=tmp_path, format="png", prog="dot")
    nx.utils.default_opener(tmp_path)


class Alphabet(object):
    NULL_CHARACTER_BASE = "#"
    LETTERS = [""] #[chr(x+48) for x in range(26)]
    SEPARATOR = "_"
    NULL_CHARACTER = NULL_CHARACTER_BASE + SEPARATOR
    NULL_LEN = len(NULL_CHARACTER)

    def __init__(self, size):
        self.alphabet = self.generate_alphabet(size, include_null_character=False)


    def get_letter_for_action_index(self, action_index):
        """ Returns the letter for the action index.
        action_index starts at 0.
        """
        return self.alphabet[action_index]

    @staticmethod
    def get_separator():
        """ Returns the separator character. """
        return Alphabet.SEPARATOR

    @staticmethod
    def get_null_character():
        """ Returns the null character """
        return Alphabet.NULL_CHARACTER

    @staticmethod
    def get_null_character_without_separator():
        """ Returns the null character """
        return Alphabet.NULL_CHARACTER_BASE

    @staticmethod
    def get_null_character_size():
        """ Returns the size of the null character. """
        return Alphabet.NULL_LEN

    @staticmethod
    def generate_alphabet(size, include_null_character=True):
        """ Generates and Alphabet of size, size.
        Alphabet will look like:
        alphabet = ["A0_",...,"Z0_", "A1_", ...,"Z1_",...]
        """
        alphabet_out = [Alphabet.NULL_CHARACTER+SEPARATOR] if include_null_character else []

        total_letters_size = len(Alphabet.LETTERS)
        loops_through_alphabet = 0

        done = False

        while not done:
            if size<=total_letters_size:
                alphabet_out += [ letter+str(loops_through_alphabet)+Alphabet.SEPARATOR for letter in Alphabet.LETTERS[:size] ]
                done=True

            elif size>total_letters_size:
                alphabet_out += [ letter+str(loops_through_alphabet)+Alphabet.SEPARATOR for letter in Alphabet.LETTERS ]
                size -= total_letters_size
                loops_through_alphabet += 1
            else:
                raise Exception(f"Size is less than 0.{size}")

        return alphabet_out


class Edgelabel(object):
    """ Class to deal with label names. """
    LABEL_NAME = "label"

    @staticmethod
    def get_param_dict(label_value):
        return {Edgelabel.LABEL_NAME : label_value}

    @staticmethod
    def get_label_name():
        return Edgelabel.LABEL_NAME
####################################################
# MAIN
####################################################


# EOF
