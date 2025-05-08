# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:37:50 2025

@author: office
"""

import turtle

# Koordinat untuk bentuk bintang
star_shape = ((0, 0), (100, 50), (50, 100), (-50, 100), (-100, 50), (0, 0))

# Registrasi bentuk baru
turtle.register_shape("bintang", star_shape)

# Gunakan bentuk kustom
t = turtle.Turtle()
t.shape("bintang")