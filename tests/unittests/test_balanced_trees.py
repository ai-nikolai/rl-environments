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
import unittest


# >>>>>>  Package Imports <<<<<<<

# >>>>>>  Local Imports   <<<<<<<
from rlenvs.mdps import BalancedDenseTreeDeterministicMDP

####################################################
# CODE
####################################################
class BalancedTreesTestCase(unittest.TestCase):
    """ Basic Tests for maths utils. """
    def test_dense_deterministic_tree_basics(self):
        branching = 2
        depth = 1
        env = BalancedDenseTreeDeterministicMDP(branching=branching, depth=depth)
        r, o, finished, state = env.step(1)

        print(o)

        self.assertGreaterEqual(r, 0, "Reward of default Agent is in [0,1]")
        self.assertGreaterEqual(1, r, "Reward of default Agent is in [0,1]")
        self.assertTrue(finished)
        self.assertEqual(o, state)

    def test_dense_deterministic_tree_two_steps(self):
        branching = 3
        depth = 2
        env = BalancedDenseTreeDeterministicMDP(branching=branching, depth=depth)
        _,o1, finished_1 , st1 = env.step(2)
        r, o2, finished_2, st2 = env.step(1)

        self.assertGreaterEqual(r, 0, "Reward of default Agent is in [0,1]")
        self.assertGreaterEqual(1, r, "Reward of default Agent is in [0,1]")
        self.assertTrue(not finished_1)
        self.assertTrue(finished_2)
        self.assertEqual(o1, st1)
        self.assertEqual(o2, st2)

    def test_dense_deterministic_tree_left_right_strategy_right(self):
        branching = 2
        depth = 3
        env = BalancedDenseTreeDeterministicMDP(branching=branching, depth=depth, reward_range=[99,102])
        r1, _, _ , _ = env.step(1)
        r2, _, _ , _ = env.step(1)
        r3, _, _ , _ = env.step(1)

        self.assertEqual(r1,99)
        self.assertEqual(r2,102)
        self.assertEqual(r3,99)


    def test_dense_deterministic_tree_left_right_strategy_optimal(self):
        branching = 2
        depth = 3
        env = BalancedDenseTreeDeterministicMDP(branching=branching, depth=depth, reward_range=[99,102])
        r1, _, _ , _ = env.step(0)
        r2, _, _ , _ = env.step(1)
        r3, _, _ , _ = env.step(0)

        self.assertEqual(r1,102)
        self.assertEqual(r2,102)
        self.assertEqual(r3,102)

    def test_dense_deterministic_tree_specs(self):
        branching = 2
        depth = 3
        env = BalancedDenseTreeDeterministicMDP(branching=branching, depth=depth, reward_range=[99,102], )
        specs = env.get_specs()

        self.assertEqual(specs["branching"],branching)
        self.assertEqual(specs["depth"], depth)
        self.assertEqual(specs["rewards"][0],99)
        self.assertEqual(specs["rewards"][1],102)

####################################################
# MAIN
####################################################


# EOF
