import Tkinter
import time
import pygame as pg     #Import the necacery modules
import os
import tkFileDialog
import sys
import alsaaudio
import audioop
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  #Set Pin numbering mode of GPIO
GPIO.setwarnings(False) #Turn warnings off
GPIO.setup(12, GPIO.IN) #Set GPIO inputs
GPIO.setup(16, GPIO.IN)

GPIO.add_event_detect(12, GPIO.RISING) #Detect rising peaks of GPIO
GPIO.add_event_detect(16, GPIO.RISING)

from Tkinter import *

import Tkinter as tk       #Import Tkinter
root = tk.Tk()               #Bind Tkinter to the root object
root.geometry("800x600")             #Set the window dimensions

root.attributes('-fullscreen', True) #Start the program in full screen



    # set up the mixer
freq = 44100     # audio CD quality
bitsize = -8    # unsigned 16 bit
channels = 8     # number of channels
buffer = 4096   # number of samples (experiment to get best sound)
pg.mixer.init(freq, bitsize, channels, buffer)
volume = 0.8


def play_music(kicksample, volume):
    pg.mixer.music.set_volume(volume)
    try:
        pg.mixer.Channel(1)
        pg.mixer.music.load(kicksample)
        print("Music file {} played!".format(kicksample))
    except pg.error:
        print("File {} not found! ({})".format(kicksample,
                                               ))
        return
    pg.mixer.music.play()


def play_music(snaresample, volume):
    
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
 
    try:
        pg.mixer.Channel(4)
        pg.mixer.music.load(snaresample)
        print("Music file {} played!".format(snaresample))
    except pg.error:
        print("File {} not found! ({})".format(snaresample, pg.get_error()))
        return
    pg.mixer.music.play()
  




#Select the sample to play

def browse_file_snare():
        global snaresample
        root.attributes('-fullscreen', False)
        snaresample = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.wav"), ("All files", "*")))
        Tk().withdraw()     
        print ('File Selected!')
        pg.mixer.music.load(snaresample)
        pg.mixer.music.play()
        root.attributes('-fullscreen', True)



def browse_file_kick():
        global kicksample
        root.attributes('-fullscreen', False)
        kicksample = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.wav"), ("All files", "*")))
        Tk().withdraw()     
        print ('File Selected!')
        pg.mixer.music.load(kicksample)
        pg.mixer.music.play()
        root.attributes('-fullscreen', True)




#upon opening your selected samples are played back



"""play_music(kicksample, volume)
time.sleep(1) # delays for 5 seconds
play_music(snaresample, volume)"""



def KickPressed():                          #Play kick when button is pressed
            play_music(kicksample, volume)
            time.sleep(0.001)

def SnarePressed():                          #Play snare when button is pressed
            play_music(snaresample, volume)
            time.sleep(0.001)






root.attributes('-fullscreen', True)

Kbutton = Button(root, text = 'Kick', command = KickPressed)         #Button For Kick
Kbutton.grid(row=0, column=2, padx=10, pady=10)                                      #Set position

 

Sbutton = Button(root, text = 'Snare', command = SnarePressed)      #Button For Snare
Sbutton.grid(row=2, column=2,padx=10, pady=10)


               
root.wm_title("Browse kick sounds")
broButton = Tkinter.Button(master = root, text = 'Browse kick sounds', width = 20, command=browse_file_kick)
broButton.grid(row=0, column=0,padx=10, pady=10)


root.wm_title("Browse snare sounds")
broButton = Tkinter.Button(master = root, text = 'Browse snare sounds', width = 20, command=browse_file_snare)
broButton.grid(row=2, column=0,padx=10, pady=10)
root.attributes('-fullscreen', True)

snaresample = ''
introtune = ''
kicksample = ''

  
    if GPIO.event_detected(12):
        KickPressed()

    if GPIO.event_detected(16):
         SnarePressed()

root.mainloop()

