#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: anelmusic
"""
import tensorflow as tf
assert tf.test.gpu_device_name(), "Your GPU is not utilized"

import numpy as np
import cv2 as cv2

import model
import aigig_utils
import music_player
import config

def main():
    # Get datasets, demo data and model
    train_generator, validation_generator = aigig_utils.get_dataset_from_paths(config.TRAIN_DIR, config.VALIDATION_DIR, config.BATCH_SIZE, config.IMG_SIZE)
    demo_imgs, demo_img_paths = aigig_utils.get_demo_data(config.TEST_DIR)
    gig_model = model.get_model(config.IMG_SIZE)
    
    if config.MODE == "train":     
        gig_model.fit(train_generator, validation_data=validation_generator, 
                      epochs=config.EPOCHS, batch_size=config.BATCH_SIZE)
        gig_model.save_weights(config.CHECKPOINT_PATH)
        print("VAL_SET train results: ", gig_model.evaluate(validation_generator))
        print("TRAIN_SET train results: ", gig_model.evaluate(train_generator))
    elif config.MODE == "inference":
        gig_model.load_weights(config.CHECKPOINT_PATH)
        print("VAL_SET train results: ", gig_model.evaluate(validation_generator))
        print("TRAIN_SET train results: ", gig_model.evaluate(train_generator))
        
    player = music_player.MusicPlayer(config.SOUND_FILE_PIANO, config.SOUND_FILE_GUITAR, config.SOUND_FILE_VIOLIN)  
    for idx, demo_img in enumerate(demo_imgs):
        img = aigig_utils.preprocess_image(demo_img, config.IMG_SIZE)
        result = gig_model.predict(img)
        prediction = np.argmax(result) # [prediction is One-Hot encoded vector]
        aigig_utils.displayImage(idx, demo_img_paths, config.DISPLAY_SIZE)
        player.updateMusic(prediction)

    player.stopMusic()    
    cv2.destroyAllWindows()

      
    
    input("EINGABE:   ")
    exit()
    

if __name__=='__main__':
    main()