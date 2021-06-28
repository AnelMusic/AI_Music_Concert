#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: anelmusic
"""

import tensorflow as tf

def get_model(image_size):
    
    # Create the base model from the pre-trained model MobileNet V2
    IMG_SHAPE = image_size + (3,)
    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                   include_top=False,
                                                   weights='imagenet')
    
    base_model.trainable = False

    # Define data augmentation sequence
    data_augmentation = tf.keras.Sequential([
      tf.keras.layers.experimental.preprocessing.RandomFlip('horizontal'),
      tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
      tf.keras.layers.experimental.preprocessing.RandomContrast(factor=0.1)
      ])
    
    preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
    global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
    prediction_layer = tf.keras.layers.Dense(4, activation = "softmax")
    
    # Define model using Funtional API
    inputs = tf.keras.Input(shape=(image_size[0], image_size[1], 3))
    x = data_augmentation(inputs)
    x = preprocess_input(x)
    x = base_model(x, training=False)
    x = global_average_layer(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = prediction_layer(x)
    model = tf.keras.Model(inputs, outputs)
    
    model.compile(loss = 'categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    
    return model
