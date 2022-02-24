#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Februar 24, 2022, at 09:51
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
    size=[1920, 1080], fullscr=True, screen=1, 
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
    opacity=None, depth=-1.0, interpolate=True)
fix_point_ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='fix_point_ISI')

# Initialize components for Routine "trial_2D"
trial_2DClock = core.Clock()
# Importieren der relevanten / benötigten Libraries
import random # für Zugriff auf die random- und shuffle-Methode

# Erstellen der Liste mit den Bild-Indices
# Da die Bilder von 1-15 durchnummeriert sind (z.B. correct1.png), wird eine Liste mit 
# entsprechenden Integern angelegt
img_index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Randomisierung der Liste mit den Bild-Indices
# wenn als Pfad zur Bilddatei $#Stimuli_2D/target' + str(img_index[trials.thisN]) + '.png'
# verwendet wird, erhält man eine zufällige Reihenfolge der Bilddateien,
# da die img_index-Liste vorher geshuffelt wurde
random.shuffle(img_index)

trial_2D_mouse = event.Mouse(win=win)
x, y = [None, None]
trial_2D_mouse.mouseClock = core.Clock()
img_correct = visual.ImageStim(
    win=win,
    name='img_correct', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(300, 278),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
img_target = visual.ImageStim(
    win=win,
    name='img_target', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(300, 278),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
img_wrong = visual.ImageStim(
    win=win,
    name='img_wrong', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(300, 278),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "instructions_3D"
instructions_3DClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Die folgenden Figuren müssen verglichen werden. Überlappen die Figuren durch Drehen vollständig, dann drücken Sie die Pfeiltaste nach OBEN, wenn nicht, drücken Sie die Pfeiltaste nach UNTEN. \n\nZum Fortfahren bitte LEERTASTE drücken.',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
trials_2D = data.TrialHandler(nReps=0.0, method='random', 
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
    # Logging der Pfade der verwendeten Bilddateien
    # Diese Variablen werden in die Experimental-csv-Daatei geschrieben und
    # als Pfad für die image-Stimuli verwendet
    img_correct_path = 'Stimuli_2d/correct' + str(img_index[trials_2D.thisN]) + '.png' # Pfad des korrekten 2D-Bildes
    img_wrong_path = 'Stimuli_2d/wrong' + str(img_index[trials_2D.thisN]) + '.png' # Pfad des falschen 2D-Bildes
    img_target_path = 'Stimuli_2d/target' + str(img_index[trials_2D.thisN]) + '.png' # Pfad des Target-Bildes
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
            img_correct.setImage(img_correct_path)
            img_target.setImage(img_target_path)
            img_wrong.setImage(img_wrong_path)
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
    # Festlegen der x-Position der Correct- und 
    # Wrong-Stimuli / Bilder
    # x_pos_correct wird bei dem Bildstimulus
    # img_correct, -x_pos_correct bei dem 
    # Bildstimulus img_wrong unter Position als x-Koordinate
    # verwendet. Der Wert 250 ist arbiträr gewählt, die
    # Anordnung der Stimuli ähnelt aber der in der 
    # Aufgabenstellung vorgegebenen Anordnung.
    if random.random() < 0.5:
        x_pos_correct = -250
    else:
        x_pos_correct = 250
    # setup some python lists for storing info about the trial_2D_mouse
    trial_2D_mouse.x = []
    trial_2D_mouse.y = []
    trial_2D_mouse.leftButton = []
    trial_2D_mouse.midButton = []
    trial_2D_mouse.rightButton = []
    trial_2D_mouse.time = []
    trial_2D_mouse.clicked_name = []
    trial_2D_mouse.clicked_pos = []
    gotValidClick = False  # until a click is received
    trial_2D_mouse.mouseClock.reset()
    img_correct.setPos((x_pos_correct, -139))
    img_target.setPos((0, 139))
    img_wrong.setPos((-x_pos_correct, -139))
    # keep track of which components have finished
    trial_2DComponents = [trial_2D_mouse, img_correct, img_target, img_wrong]
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
        # *trial_2D_mouse* updates
        if trial_2D_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_2D_mouse.frameNStart = frameN  # exact frame index
            trial_2D_mouse.tStart = t  # local t and not account for scr refresh
            trial_2D_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_2D_mouse, 'tStartRefresh')  # time at next scr refresh
            trial_2D_mouse.status = STARTED
            prevButtonState = trial_2D_mouse.getPressed()  # if button is down already this ISN'T a new click
        if trial_2D_mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_2D_mouse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                trial_2D_mouse.tStop = t  # not accounting for scr refresh
                trial_2D_mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_2D_mouse, 'tStopRefresh')  # time at next scr refresh
                trial_2D_mouse.status = FINISHED
        if trial_2D_mouse.status == STARTED:  # only update if started and not finished!
            buttons = trial_2D_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(img_correct)
                        clickableList = img_correct
                    except:
                        clickableList = [img_correct]
                    for obj in clickableList:
                        if obj.contains(trial_2D_mouse):
                            gotValidClick = True
                            trial_2D_mouse.clicked_name.append(obj.name)
                            trial_2D_mouse.clicked_pos.append(obj.pos)
                    x, y = trial_2D_mouse.getPos()
                    trial_2D_mouse.x.append(x)
                    trial_2D_mouse.y.append(y)
                    buttons = trial_2D_mouse.getPressed()
                    trial_2D_mouse.leftButton.append(buttons[0])
                    trial_2D_mouse.midButton.append(buttons[1])
                    trial_2D_mouse.rightButton.append(buttons[2])
                    trial_2D_mouse.time.append(trial_2D_mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
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
    # Speichern der x-Koordinaten der Stimuli
    # x_pos_correct = x-Position (pix) der img_correct-Stimuli
    # x_pos_wrong = x-Position (pix) der img_wrong-Stimuli
    thisExp.addData('x_pos_correct', x_pos_correct)
    thisExp.addData('x_pos_wrong', -x_pos_correct)
    
    # Speichern der verwendeten Bilddateien
    # (in den csv-Dateien kann man anhand der Zahlern
    # der verwendeten Bilder sehen, dass die Stimuli
    # randomisiert präsentiert werden)
    thisExp.addData('img_correct', img_correct_path)
    thisExp.addData('img_wrong', img_wrong_path)
    thisExp.addData('img_target', img_target_path)
    # store data for trials_2D (TrialHandler)
    if len(trial_2D_mouse.x): trials_2D.addData('trial_2D_mouse.x', trial_2D_mouse.x[0])
    if len(trial_2D_mouse.y): trials_2D.addData('trial_2D_mouse.y', trial_2D_mouse.y[0])
    if len(trial_2D_mouse.leftButton): trials_2D.addData('trial_2D_mouse.leftButton', trial_2D_mouse.leftButton[0])
    if len(trial_2D_mouse.midButton): trials_2D.addData('trial_2D_mouse.midButton', trial_2D_mouse.midButton[0])
    if len(trial_2D_mouse.rightButton): trials_2D.addData('trial_2D_mouse.rightButton', trial_2D_mouse.rightButton[0])
    if len(trial_2D_mouse.time): trials_2D.addData('trial_2D_mouse.time', trial_2D_mouse.time[0])
    if len(trial_2D_mouse.clicked_name): trials_2D.addData('trial_2D_mouse.clicked_name', trial_2D_mouse.clicked_name[0])
    if len(trial_2D_mouse.clicked_pos): trials_2D.addData('trial_2D_mouse.clicked_pos', trial_2D_mouse.clicked_pos[0])
    trials_2D.addData('trial_2D_mouse.started', trial_2D_mouse.tStart)
    trials_2D.addData('trial_2D_mouse.stopped', trial_2D_mouse.tStop)
    trials_2D.addData('img_correct.started', img_correct.tStartRefresh)
    trials_2D.addData('img_correct.stopped', img_correct.tStopRefresh)
    trials_2D.addData('img_target.started', img_target.tStartRefresh)
    trials_2D.addData('img_target.stopped', img_target.tStopRefresh)
    trials_2D.addData('img_wrong.started', img_wrong.tStartRefresh)
    trials_2D.addData('img_wrong.stopped', img_wrong.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials_2D'


# ------Prepare to start Routine "instructions_3D"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instructions_3DComponents = [text]
for thisComponent in instructions_3DComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_3DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_3D"-------
while continueRoutine:
    # get current time
    t = instructions_3DClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_3DClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_3DComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_3D"-------
for thisComponent in instructions_3DComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instructions_3D" was not non-slip safe, so reset the non-slip timer
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
