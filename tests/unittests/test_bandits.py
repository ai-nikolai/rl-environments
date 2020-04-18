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
from rlenvs.bandits import MultiarmBernoulliBandit

####################################################
# CODE
####################################################
class BanditsTestCase(unittest.TestCase):
    """ Basic Tests for maths utils. """
    def test_bernoulli_bandit_returns_correct_reward_and_step(self):
        arms = 4
        env = MultiarmBernoulliBandit(arms)
        r, o, finished, state = env.step(3)

        self.assertIn(r, [0,1], "Reward of Bernouli Agent is not in [0,1]")
        self.assertIsNone(o)
        self.assertTrue(not finished)
        self.assertIsNone(state)


    def test_bernoulli_bandit_can_be_initialised_correctly(self):
        probabilities = [0.1,0.2]
        env = MultiarmBernoulliBandit(arms=3, success_probabilities=probabilities)
        env.seed(99)

        arms, probs, seed = env.get_specs()

        self.assertEqual(arms, 2)
        self.assertListEqual(probs, probabilities)
        self.assertEqual(seed, 99)



####################################################
# MAIN
####################################################


# EOF
