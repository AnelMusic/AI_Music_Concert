#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: anelmusic
"""
import glob

import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator

import numpy as np
from PIL import Image

import cv2 as cv2


def preprocess_image(img, img_size):
    img = tf.keras.layers.experimental.preprocessing.Resizing(
        img_size[0],img_size[1])(img)
    img = np.expand_dims(img, axis=0)
    
    return img

def get_dataset_from_paths(train_dir, validation_dir, BATCH_SIZE, IMG_SIZE):   
    TRAINING_DIR = train_dir
    VALIDATION_DIR = validation_dir
    
    # traindata generator
    training_datagen = ImageDataGenerator(
        rotation_range=40, 
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
        )
    
    train_generator = training_datagen.flow_from_directory(
        TRAINING_DIR, 
        target_size=IMG_SIZE,
        class_mode='categorical',
        batch_size=BATCH_SIZE
        )

    # traindata generator (no augmentation)
    validation_datagen = ImageDataGenerator()

    validation_generator = validation_datagen.flow_from_directory(
        VALIDATION_DIR, 
        target_size=IMG_SIZE,
        class_mode='categorical',
        batch_size=BATCH_SIZE
        )

    return train_generator, validation_generator



def get_demo_data(demo_dir):
    filelist = glob.glob(demo_dir+"/*.png")
    filelist.sort()
    img_list = [np.asarray(Image.open(img)) for img in filelist]
    
    return img_list, filelist

def displayImage(idx, demo_img_paths, display_size):
    display_img = cv2.imread(demo_img_paths[idx])
    resized = cv2.resize(display_img, display_size, interpolation = cv2.INTER_AREA)
    cv2.imshow("AI_GIG",resized)
    cv2.waitKey(15) # ms
