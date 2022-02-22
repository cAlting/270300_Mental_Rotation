#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Februar 22, 2022, at 20:36
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

# Initialize components for Routine "ITI_Fixation_2D"
ITI_Fixation_2DClock = core.Clock()
fix_point = visual.ShapeStim(
    win=win, name='fix_point',units='pix', 
    size=(10, 10), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
fix_point_ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='fix_point_ISI')

# Initialize components for Routine "trial_2D"
trial_2DClock = core.Clock()
# Importieren der relevanten / benötigten Libraries
import random # für Zugriff auf die random- und shuffle-Methode

# Anlegen eines Trial-Index, um verfolgen zu können, in welchem Trial man sich gerade befindet
# (Dies ist ein Workaround, da lt. Foren trials.thisN oder trials.trialsThisN nicht richtig funktioniert;
# diese Erfahrung habe ich auch im Seminar schon gemacht)
trial_index = 0

# Erstellen der Liste mit den Bild-Indices
# Da die Bilder von 1-15 durchnummeriert sind, wird eine Liste mit entsprechenden Integern angelegt
img_index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Randomisierung der Liste mit den Bild-Indices
# wenn als Pfad zur Bilddatei $#Stimuli_2D/target' + str(img_index[trials.thisN]) + '.png'
# verwendet wird, erhält man eine zufällige Reihenfolge der Bilddateien,
# da die img_index-Liste vorher geshuffelt wurde
random.shuffle(img_index)

img_correct = visual.ImageStim(
    win=win,
    name='img_correct', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(300, 278),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
img_target = visual.ImageStim(
    win=win,
    name='img_target', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(300, 278),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
img_wrong = visual.ImageStim(
    win=win,
    name='img_wrong', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(300, 278),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

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

# set up handler to look after randomisation of conditions etc
trials_2D = data.TrialHandler(nReps=15.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2D')
thisExp.addLoop(trials_2D)  # add the loop to the experiment
thisTrials_2D = trials_2D.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_2D.rgb)
if thisTrials_2D != None:
    for paramName in thisTrials_2D:
        exec('{} = thisTrials_2D[paramName]'.format(paramName))

for thisTrials_2D in trials_2D:
    currentLoop = trials_2D
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_2D.rgb)
    if thisTrials_2D != None:
        for paramName in thisTrials_2D:
            exec('{} = thisTrials_2D[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI_Fixation_2D"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_Fixation_2DComponents = [fix_point, fix_point_ISI]
    for thisComponent in ITI_Fixation_2DComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_Fixation_2DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI_Fixation_2D"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_Fixation_2DClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_Fixation_2DClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_point* updates
        if fix_point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_point.frameNStart = frameN  # exact frame index
            fix_point.tStart = t  # local t and not account for scr refresh
            fix_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_point, 'tStartRefresh')  # time at next scr refresh
            fix_point.setAutoDraw(True)
        if fix_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_point.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_point.tStop = t  # not accounting for scr refresh
                fix_point.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_point, 'tStopRefresh')  # time at next scr refresh
                fix_point.setAutoDraw(False)
        # *fix_point_ISI* period
        if fix_point_ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            fix_point_ISI.frameNStart = frameN  # exact frame index
            fix_point_ISI.tStart = t  # local t and not account for scr refresh
            fix_point_ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_point_ISI, 'tStartRefresh')  # time at next scr refresh
            fix_point_ISI.start(1)
        elif fix_point_ISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *fix_point_ISI*
            img_correct.setImage('Stimuli_2d/correct' + str(img_index[trials_2D.thisN]) + '.png')
            img_target.setImage('Stimuli_2d/target' + str(img_index[trials_2D.thisN]) + '.png')
            img_wrong.setImage('Stimuli_2d/wrong' + str(img_index[trials_2D.thisN]) + '.png')
            # component updates done
            fix_point_ISI.complete()  # finish the static period
            fix_point_ISI.tStop = fix_point_ISI.tStart + 1  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_Fixation_2DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_Fixation_2D"-------
    for thisComponent in ITI_Fixation_2DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2D.addData('fix_point.started', fix_point.tStartRefresh)
    trials_2D.addData('fix_point.stopped', fix_point.tStopRefresh)
    trials_2D.addData('fix_point_ISI.started', fix_point_ISI.tStart)
    trials_2D.addData('fix_point_ISI.stopped', fix_point_ISI.tStop)
    
    # ------Prepare to start Routine "trial_2D"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    trial_index += 1
    
    if random.random() < 0.5:
        x_pos_correct = -250
    else:
        x_pos_correct = 250
    img_correct.setPos((x_pos_correct, -139))
    img_target.setPos((0, 139))
    img_wrong.setPos((-x_pos_correct, -139))
    # keep track of which components have finished
    trial_2DComponents = [img_correct, img_target, img_wrong]
    for thisComponent in trial_2DComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_2DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_2D"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_2DClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_2DClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_correct* updates
        if img_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_correct.frameNStart = frameN  # exact frame index
            img_correct.tStart = t  # local t and not account for scr refresh
            img_correct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_correct, 'tStartRefresh')  # time at next scr refresh
            img_correct.setAutoDraw(True)
        if img_correct.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_correct.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                img_correct.tStop = t  # not accounting for scr refresh
                img_correct.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_correct, 'tStopRefresh')  # time at next scr refresh
                img_correct.setAutoDraw(False)
        
        # *img_target* updates
        if img_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_target.frameNStart = frameN  # exact frame index
            img_target.tStart = t  # local t and not account for scr refresh
            img_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_target, 'tStartRefresh')  # time at next scr refresh
            img_target.setAutoDraw(True)
        if img_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_target.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                img_target.tStop = t  # not accounting for scr refresh
                img_target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_target, 'tStopRefresh')  # time at next scr refresh
                img_target.setAutoDraw(False)
        
        # *img_wrong* updates
        if img_wrong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_wrong.frameNStart = frameN  # exact frame index
            img_wrong.tStart = t  # local t and not account for scr refresh
            img_wrong.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_wrong, 'tStartRefresh')  # time at next scr refresh
            img_wrong.setAutoDraw(True)
        if img_wrong.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_wrong.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                img_wrong.tStop = t  # not accounting for scr refresh
                img_wrong.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_wrong, 'tStopRefresh')  # time at next scr refresh
                img_wrong.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2D"-------
    for thisComponent in trial_2DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2D.addData('img_correct.started', img_correct.tStartRefresh)
    trials_2D.addData('img_correct.stopped', img_correct.tStopRefresh)
    trials_2D.addData('img_target.started', img_target.tStartRefresh)
    trials_2D.addData('img_target.stopped', img_target.tStopRefresh)
    trials_2D.addData('img_wrong.started', img_wrong.tStartRefresh)
    trials_2D.addData('img_wrong.stopped', img_wrong.tStopRefresh)
    thisExp.nextEntry()
    
# completed 15.0 repeats of 'trials_2D'


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
