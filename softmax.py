# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 00:07:49 2017

@author: ellie
"""

# Solution is available in the other "solution.py" tab
import numpy as np


def softmax(z):
    """Compute softmax values for each sets of scores in z."""
    # TODO: Compute and return softmax(z)
    return np.exp(z) / np.sum(np.exp(z), axis=0)
logits = [3.0, 1.0, 0.2]
print(softmax(logits))
