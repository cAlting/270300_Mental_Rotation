#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Februar 22, 2022, at 13:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = '270300_Mental_Rotation'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\calti\\Documents\\GitHub\\270300_Mental_Rotation\\270300_Mental_Rotation_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[3440, 1440], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions_2D"
instructions_2DClock = core.Clock()
instr_2D = visual.ImageStim(
    win=win,
    name='instr_2D', units='pix', 
    image='Stimuli_2D/instructions/instructions.png', mask=None,
    ori=0.0, pos=(0, 0), size=(584, 441),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_kb = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions_2D"-------
continueRoutine = True
# update component parameters for each repeat
instr_kb.keys = []
instr_kb.rt = []
_instr_kb_allKeys = []
# keep track of which components have finished
instructions_2DComponents = [instr_2D, instr_kb]
for thisComponent in instructions_2DComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_2DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_2D"-------
while continueRoutine:
    # get current time
    t = instructions_2DClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_2DClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2D* updates
    if instr_2D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2D.frameNStart = frameN  # exact frame index
        instr_2D.tStart = t  # local t and not account for scr refresh
        instr_2D.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2D, 'tStartRefresh')  # time at next scr refresh
        instr_2D.setAutoDraw(True)
    
    # *instr_kb* updates
    waitOnFlip = False
    if instr_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_kb.frameNStart = frameN  # exact frame index
        instr_kb.tStart = t  # local t and not account for scr refresh
        instr_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_kb, 'tStartRefresh')  # time at next scr refresh
        instr_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_kb.status == STARTED and not waitOnFlip:
        theseKeys = instr_kb.getKeys(keyList=['space'], waitRelease=False)
        _instr_kb_allKeys.extend(theseKeys)
        if len(_instr_kb_allKeys):
            instr_kb.keys = _instr_kb_allKeys[-1].name  # just the last key pressed
            instr_kb.rt = _instr_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_2D"-------
for thisComponent in instructions_2DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_2D.started', instr_2D.tStartRefresh)
thisExp.addData('instr_2D.stopped', instr_2D.tStopRefresh)
# check responses
if instr_kb.keys in ['', [], None]:  # No response was made
    instr_kb.keys = None
thisExp.addData('instr_kb.keys',instr_kb.keys)
if instr_kb.keys != None:  # we had a response
    thisExp.addData('instr_kb.rt', instr_kb.rt)
thisExp.addData('instr_kb.started', instr_kb.tStartRefresh)
thisExp.addData('instr_kb.stopped', instr_kb.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_2D" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
