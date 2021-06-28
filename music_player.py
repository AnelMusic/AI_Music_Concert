#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: anelmusic
"""
import pygame.mixer
import pygame

class MusicPlayer():
    def __init__(self, sound_file_piano, sound_file_guitar, sound_file_violin):
        self.__initMixer(sound_file_piano, sound_file_guitar, sound_file_violin)    
    
    def __initMixer(self, sound_file_piano, sound_file_guitar, sound_file_violin):
        MULTI_MIXER = pygame.mixer    
        MULTI_MIXER.pre_init(44100, -16, 2, 2048) # see.Pygame MutiMixerDoc
        MULTI_MIXER.init()
        
        self.PIANO_MIXER = MULTI_MIXER.Channel(0)
        self.GUITAR_MIXER = MULTI_MIXER.Channel(1)
        self.VIOLIN_MIXER = MULTI_MIXER.Channel(2)
        
        self.PIANO_MIXER.play(pygame.mixer.Sound(sound_file_piano))
        self.PIANO_MIXER.pause()
        self.GUITAR_MIXER.play(pygame.mixer.Sound(sound_file_guitar))
        self.GUITAR_MIXER.pause()
        self.VIOLIN_MIXER.play(pygame.mixer.Sound(sound_file_violin))
        self.VIOLIN_MIXER.pause()
        
    def updateMusic(self, prediction):
        if prediction == 1:            
            self.PIANO_MIXER.pause()
            self.GUITAR_MIXER.pause() 
            self.VIOLIN_MIXER.pause()
        elif prediction == 2:
            self.PIANO_MIXER.pause()
            self.GUITAR_MIXER.pause() 
            self.VIOLIN_MIXER.pause()
            self.PIANO_MIXER.unpause()
        elif prediction == 0:
            self.PIANO_MIXER.pause()
            self.GUITAR_MIXER.pause() 
            self.VIOLIN_MIXER.pause()
            self.GUITAR_MIXER.unpause()
        elif prediction == 3:
            self.PIANO_MIXER.pause()
            self.GUITAR_MIXER.pause() 
            self.VIOLIN_MIXER.pause()
            self.VIOLIN_MIXER.unpause()
    
    def stopMusic(self):
            self.PIANO_MIXER.stop() 
            self.GUITAR_MIXER.stop() 
            self.VIOLIN_MIXER.stop()
            
        
        
    
    
        