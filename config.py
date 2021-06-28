#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 01:46:35 2021

@author: anelmusic
"""

"Provide path to music files"
##############################################################################
SOUND_FILE_PIANO = '/home/anelmusic/Desktop/1.ogg'
SOUND_FILE_GUITAR= '/home/anelmusic/Desktop/2.ogg'
SOUND_FILE_VIOLIN = '/home/anelmusic/Desktop/3.ogg'

"Provide path to datasets"
##############################################################################
TRAIN_DIR = "/home/anelmusic/anel_projects/ai_gig/data/train"
VALIDATION_DIR = "/home/anelmusic/anel_projects/ai_gig/data/val"
TEST_DIR = "/home/anelmusic/anel_projects/ai_gig/data/test_demo"

"Define Basic Hyperparams"
##############################################################################
BATCH_SIZE = 64
EPOCHS = 10
IMG_SIZE = (224, 224) # MobileNetV2 Epexts 224 squared inputs
MODE = "train" # train/inference

"Define additional params"
##############################################################################       
DISPLAY_SIZE = (228,172) # Size of displayed image form stream
CHECKPOINT_PATH = "./checkpoints/my_checkpoint"
