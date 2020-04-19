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
from rlenvs.utils import BaseEnvironment, maths_utils, tree_utils


####################################################
# CODE
####################################################
class BalancedDenseTreeDeterministicMDP(BaseEnvironment):
    """ This creates MDPs that have. """
    def __init__(self,
            branching=2,
            depth=2,
            reward_range=[0,1],
            distribution_strategy="left-right",
            seed=0):
        """
        Creates a tree with branching factor branching and depth depth.
        Depth 2 , branching 2 means:
              Root
            /     "\
          #0        #1
         /   \\    /   \\
        00   10  01   11

        reward_range:
        rewards are in the reward range and are distributed according to the number of branches. i.e.:
        branching = 3, reward_range=[0,1]
        rewards => [0,0.5,1]

        distribution strategy can be:
        "left" : -> taking the left most action (0) has the highest reward.
        "right" : -> taking the right most action (branching-1) has the highest reward.
        "left-right" : -> rewards alternate between being "left" or "right"
        """
        self.branching = branching
        self.depth = depth

        (self.tree, self.root_name, self.action_names) = tree_utils.generate_balanced_tree(branching=branching, depth=depth, return_all=True)

        if len(reward_range)==2:
            self.rewards = np.linspace(reward_range[0], reward_range[1], branching)
        else:
            Exception(f"Reward Range needs to be a list of two. {reward_range}")

        if self._verify_distribution_strategy( distribution_strategy):
            self.distribution_strategy = distribution_strategy

        self._seed = seed

        #things used actively
        self.previous_state = self.root_name
        self.current_state = self.root_name
        self.current_depth = 0



    def step(self, action):
        if action<self.branching and action>=0:
            reward = self._get_reward(action)
            state, finished = self._update(action)
            observation = state
            is_finished = finished
            state = state
            return reward, observation, is_finished, state
        else:
            raise Exception(f"Wrong Action({action}) for branching{self.branching}")


    def undo(self):
        raise NotImplementedError

    def go_to_state(self,state):
        raise NotImplementedError

    def seed(self,seed):
        self._seed = seed

    def render(self):
        print(self.success_probabilities)

    def get_specs(self):
        """ Returns specs of tree based MDP. """
        specs_dictionary = {
            "action_names" : self.action_names,
            "rewards" : self.rewards,
            "distribution_strategy" : self.distribution_strategy,
            "branching" : self.branching,
            "depth" : self.depth,
            "seed" : self._seed,
        }

        return specs_dictionary


    def _update(self,action):
        """ updates self according to action. """
        next_steps = list(self.tree.successors(self.current_state))
        finished = True
        if next_steps:
            self.previous_state = self.current_state
            self.current_state = next_steps[action]
            self.current_depth += 1
            next_steps = list(self.tree.successors(self.current_state))
            if next_steps: #it makes sense to continue
                finished = False

        return self.current_state, finished


    def _get_reward(self, action):
        """ returns the reward accoridng to distribution strategy. """
        if self.distribution_strategy=="left-right":
            left_flag = True if self.current_depth%2==0 else False
            current_rewards = np.flip(self.rewards) if left_flag else self.rewards
            return current_rewards[action]


    def _verify_distribution_strategy(self, distribution_strategy):
        """
        Can be:
            left, right, left-right,...
        """
        allowed_values = ["left","right","left-right"]
        implemented_values = ["left-right"]

        if distribution_strategy in allowed_values:
            if distribution_strategy in implemented_values:
                return True
            else:
                raise NotImplementedError(f"Distribution Strategy is not implemented: {distribution_strategy}")
        else:
            raise Exception(f"Distribution Strategy Doesn't Exists: {distribution_strategy}")


####################################################
# MAIN
####################################################


# EOF
