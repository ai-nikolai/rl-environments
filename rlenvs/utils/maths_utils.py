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


####################################################
# CODE
####################################################

def verify_probability_vector(vector):
    """ Verifies that Vector is a probability vector. """
    if vector:
        return all( map( verify_probability, vector ) )
    else:
        raise ValueError("Empty Vectors are not supported.")

def verify_probability(probability):
    """ Makes sure it's a probability. """
    return probability>=0 and probability<=1

def generate_probability_vector(length):
    """ Generates a list of probabilities. """
    return list( np.random.random(length) )
####################################################
# MAIN
####################################################


# EOF
