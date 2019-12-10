#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
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

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
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


# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
stim1 = visual.TextStim(win, text='Here is Tommy. This morning Tommy brought a cupcake and he was going to eat this cupcake at snack time. Tommy put it on the table. Then, Tommy went out to play. Next, Dave came \nin and found that there was this cupcake on the table. Dave was hungry. Dave knew that \nthis cupcake is Tommy’s, but he took away the cupcake and ate it without asking Tommy.')
stim2 = visual.TextStim(win, text='Now let’s suppose that it was not the first time for Dave to take away and eat Tommy’s food. Dave kept doing this over and over. In this case, Tommy thought Dave should be treated in the same way. He thought next day he would take away Dave’s muffin from his lunch box as return.')
stim3 = visual.TextStim(win, text='Here is another story, and this is about Mike and Danny. This morning Mike brought a cupcake and he was going to eat this cupcake at snack time. He usually leaves his cupcake in the lunchbox but this time he just put this cupcake on the table. Then, Mike went out to play. Next, Danny came in and found that there was the cupcake on the table. Danny thought this is the surprise cupcake given by the teacher because the teacher sometimes gives surprise cupcake to the class. Danny thought it is his turn to take the surprise cupcake. Therefore, Danny took away the cupcake and ate it.')

scenarios = [stim1, stim2, stim3]
scenarios = pd.Dataframe(scenarios)


# make your loop
for scenario in scenarios:
    myStimulus.setText(scenario)
    myStimulus.draw()
    win.flip()
    rating = visual.RatingScale()
    
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
