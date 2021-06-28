#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 18:49:25 2021

@author: anelmusic
"""
import tensorflow as tf
import numpy as np

def say_hi():
    print("Hi")
    
def preprocess_image(img, img_size):
    
    img = tf.keras.layers.experimental.preprocessing.Resizing( img_size[0],img_size[1])(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img