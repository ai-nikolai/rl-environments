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

# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################
class BaseEnvironment(object):
    """
    Implements the following methods inspired by both OpenAI gym and Deepmind Bsuite (dm_env).

    For the light weight introduction of these environments, however, the respecitve environments from these research houses will not be used.

    In particular, also because the Specs will be custom and more experimental of these environemnts.

    :step(action) -> reward(float), observation(Optional[Any]), is_finished(bool), state(Optional[Any]):
    :reset() -> "resets the environement":
    :undo() -> "goes to the previous state of the environment" reward, observation, is_finished(bool), sate(Optional[Any]):
    :go_to_state(state) -> "goes to a specific state of the environment" is_finished(bool):
    :seed(int) -> "sets the seed":
    :render() -> "renders the environment":
    :get_specs() -> returns the custom specs of the environment:
    """

    def initialise(self):
        """ returns the first observation. """
        raise NotImplementedError

    def step(self,action):
        """ Run a single step. """
        raise NotImplementedError

    def reset(self):
        """ Resets the Environment. """
        raise NotImplementedError

    def undo(self):
        """ Undoes the last step.(if possible) """
        raise NotImplementedError

    def go_to_state(self, state):
        """ Run a single step. """
        raise NotImplementedError

    def seed(self, seed):
        """ Sets the random seed of the environment. """
        raise NotImplementedError

    def render(self):
        """ Renders the environment. """
        raise NotImplementedError

    def get_specs(self):
        """ Returns the specs of the environment. """
        raise NotImplementedError
####################################################
# MAIN
####################################################


# EOF
