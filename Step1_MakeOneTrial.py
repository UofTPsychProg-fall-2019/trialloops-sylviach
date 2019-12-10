#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# Escape method
event.globalKeys.add(key='q',func=core.quit)

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))  
myStimulus = visual.TextStim(win=win, name='Vignette',
    text='Here is Tommy. This morning Tommy brought a cupcake and he was going to eat this cupcake at snack time. Tommy put it on the table. Then, Tommy went out to play. Next, Dave came \nin and found that there was this cupcake on the table. Dave was hungry. Dave knew that \nthis cupcake is Tommy’s, but he took away the cupcake and ate it without asking Tommy.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

# then draw all stimuli
myStimulus.draw()

# then flip your window
win.flip()

# then record your responses
Rating = visual.RatingScale(win=win, name='Rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=['not okay at all', ' a little not okay', ' neutral', ' a little okay', ' very okay'], scale='How okay or not okay is this behaviour described?')



#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
