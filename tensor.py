# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:28:07 2017

@author: ellie
"""

import tensorflow as tf

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)