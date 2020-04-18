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
from rlenvs.utils import maths_utils

####################################################
# CODE
####################################################
class MathsUtilsTest(unittest.TestCase):
    """ Basic Tests for maths utils. """
    def test_verify_probability(self):
        p1 = (-0.5, False)
        p2 = (0, True)
        p3 = (0.5, True)
        p4 = (1, True)
        p5 = (1.2, False)

        self.assertEqual(maths_utils.verify_probability(p1[0]), p1[1], "-0.5 is considered a probability.")
        self.assertEqual(maths_utils.verify_probability(p2[0]), p2[1], "0 is not considered a probability")
        self.assertEqual(maths_utils.verify_probability(p3[0]), p3[1], "0.5 is not considered a probability")
        self.assertEqual(maths_utils.verify_probability(p4[0]), p4[1], "1 is not considered a probability")
        self.assertEqual(maths_utils.verify_probability(p5[0]), p5[1], "1.2 is considered a probability.")

    def test_verify_probability_vector(self):
        p1 = ([0.5,0.1,0.2,0.3], True)
        p2 = ([0.5,0.1,0.2,-0.3], False)
        p4 = ([1.2],False)
        p5 = ([0.5],True)
        p6 = ([0.1,1.2],False)

        #exception case
        p3 = ([],False)


        self.assertEqual(maths_utils.verify_probability_vector(p1[0]), p1[1], "Example 1 prob vector failed.")
        self.assertEqual(maths_utils.verify_probability_vector(p2[0]), p2[1], "Example 2 prob vector failed.")
        self.assertEqual(maths_utils.verify_probability_vector(p4[0]), p4[1], "Example 4 prob vector failed.")
        self.assertEqual(maths_utils.verify_probability_vector(p5[0]), p5[1], "Example 5 prob vector failed.")
        self.assertEqual(maths_utils.verify_probability_vector(p6[0]), p6[1], "Example 6 prob vector failed.")

        #exception case
        with self.assertRaises(ValueError):
            maths_utils.verify_probability_vector(p3[0])

####################################################
# MAIN
####################################################


# EOF
