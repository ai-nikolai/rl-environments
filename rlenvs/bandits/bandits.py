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
import numpy as np


# >>>>>>  Package Imports <<<<<<<


# >>>>>>  Local Imports   <<<<<<<
from rlenvs.utils import BaseEnvironment, maths_utils


####################################################
# CODE
####################################################
class MultiarmBernoulliBandit(BaseEnvironment):
    """ A classical Multiarm Bandit with binary Bernoulli Bandit. """
    def __init__(self,
            arms,
            success_probabilities=[],
            seed=0):
        """ Multiarm Bandit Initialisation Function.
        Uses success_probabilities if they are set, otherwise uses number of arms and initialises
        """
        if success_probabilities:
            if not maths_utils.verify_probability_vector(success_probabilities):
                raise Exception(f"Probability vector is not a probability vector.")
            self.arms = len(success_probabilities)
            self.success_probabilities = success_probabilities
        else:
            if arms<2:
                raise Exception("Too few arms")
            self.arms = arms
            self.success_probabilities = maths_utils.generate_probability_vector(arms)

        self._seed = seed


    def step(self, action):
        if action<self.arms and action>=0:
            reward = self._get_reward(action)
            observation = None
            is_finished = False
            state = None
            return reward, observation, is_finished, state
        else:
            raise Exception(f"Wrong Action({action}) for Arms{self.arms}")


    def undo(self):
        pass

    def go_to_state(self,state):
        pass

    def seed(self,seed):
        self._seed = seed

    def render(self):
        print(self.success_probabilities)

    def get_specs(self):
        """ Returns arms and success probabilities and seed. """
        specs_dictionary = {
            "arms" : self.arms,
            "success_probabilities" : self.success_probabilities,
            "seed" : self._seed,
        }
        return specs_dictionary

    def _get_reward(self, action):
        """ Gets the reward for this Env. """
        return int( np.random.binomial(1,p=self.success_probabilities[action]) )

####################################################
# MAIN
####################################################


# EOF
