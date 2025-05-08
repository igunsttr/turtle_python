# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:55:02 2025

@author: office
"""

import turtle as t
from random import random

for i in range(50):
    #steps = int(random() * 100)
    steps = 50
    angle = i
    t.right(angle)
    t.fd(steps)
    
    