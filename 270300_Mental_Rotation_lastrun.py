#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on März 07, 2022, at 21:23
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
expInfo = {'participant': '', 'session': '001', 'group': ''}
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
instr_2D_kb = keyboard.Keyboard()

# Initialize components for Routine "ITI_Fixation_2D"
ITI_Fixation_2DClock = core.Clock()
fix_point_2D = visual.ShapeStim(
    win=win, name='fix_point_2D',units='pix', 
    size=(5, 5), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
fix_point_2D_ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='fix_point_2D_ISI')

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
    ori=0.0, pos=(0, 139), size=(300, 278),
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
instr_3D = visual.TextStim(win=win, name='instr_3D',
    text='Die folgenden Figuren müssen verglichen werden. Überlappen die Figuren durch Drehen vollständig, dann drücken Sie die Pfeiltaste nach OBEN, wenn nicht, drücken Sie die Pfeiltaste nach UNTEN. \n\nZum Fortfahren bitte LEERTASTE drücken.',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_3D_kb = keyboard.Keyboard()

# Initialize components for Routine "ITI_Fixation_3D"
ITI_Fixation_3DClock = core.Clock()
fix_point_3D = visual.ShapeStim(
    win=win, name='fix_point_3D',units='pix', 
    size=(5, 5), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
fix_point_3D_ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='fix_point_3D_ISI')

# Initialize components for Routine "trial_3D"
trial_3DClock = core.Clock()
## Laden der relevanten Libraries
import os       # für OS-spezifischen Separator
import sys      # um Pfad des aktuellen Python-Skriptes auszulesen
import glob     # zum Erstellen einer Liste mit allen Bildernamen
import re


# Custom Funktion für natural sorting
# gefunden unter: https://github.com/bdrung/snippets/blob/master/natural_sorted.py
# Grund für Verwendung: Wenn Pfade zu Bilddateien per glob ausgelesen werden, wird die Reihen-
# folge verändert (xx_0, xx_100, xx_150, xx_50), da die 5 höher als 0 oder 1 ist.
# Natural Sorting sortiert die Pfadnamen so, "wie man es erwarten würde", d.h. so, als ob
# die Dateien xx_50 als xx_050 vorlägen.
def natural_sorted(iterable, key=None, reverse=False):
    """Return a new naturally sorted list from the items in *iterable*.

    The returned list is in natural sort order. The string is ordered
    lexicographically (using the Unicode code point number to order individual
    characters), except that multi-digit numbers are ordered as a single
    character.

    Has two optional arguments which must be specified as keyword arguments.

    *key* specifies a function of one argument that is used to extract a
    comparison key from each list element: ``key=str.lower``.  The default value
    is ``None`` (compare the elements directly).

    *reverse* is a boolean value.  If set to ``True``, then the list elements are
    sorted as if each comparison were reversed.

    The :func:`natural_sorted` function is guaranteed to be stable. A sort is
    stable if it guarantees not to change the relative order of elements that
    compare equal --- this is helpful for sorting in multiple passes (for
    example, sort by department, then by salary grade).
    """
    prog = re.compile(r"(\d+)")

    def alphanum_key(element):
        """Split given key in list of strings and digits"""
        return [int(c) if c.isdigit() else c for c in prog.split(key(element)
                if key else element)]

    return sorted(iterable, key=alphanum_key, reverse=reverse)




## Einlesen der Bilder
''' 
1. Pfad des Experimentes / aktuellen Python-Skriptes auslesen
Grund: wenn das Experiment auf anderen Rechnern ausgeführt wird,
       wäre ein Hardcoden des Pfades zum Experiment (z.B. der Pfad
       auf _meinem_ PC unklug, da es auf anderem PC zu Fehler käme)
 
 Erläuterung des Codes:
- sys.argv[0] ist der Name des Skriptes
- os.path.realpath(<path>) wandelt Argument in kanonischen Pfad ("kürzester Pfad i.S.v. Stringlänge"
    bzw. Pfad ohne symbolische Links, Abkürzungen wie /./../ um"), sodass der Pfad eindeutig
    und unique ist -> Output ist der kanonische Pfad der Scriptdatei
- os.path.dirname(<path>) gibt den Pfad der Inputdatei oder des Input-Directory (in Form einer Pfades 
    übergeben) aus -> Output ist der Pfad der Scriptdatei sys.argv[0]
'''
exp_root_path = os.path.dirname(os.path.realpath(sys.argv[0]))

'''
2. Abhängig vom aktuellen Block (und somit auch Gruppenzugehörigkeit, da Blockreihenfolge für Gruppe A
und B unterschiedlich) wird das Verzeichnis der zu verwendenden Bilder dynamisch festgelegt.

Erläuterungen:
    abhängig von der verwendeten Conditions-File steht in der Conditions-Spalte in Zeile 1 easy (Gruppe A) oder
    hard (Gruppe B). Für Gruppe A enthält ist Conditions[0] somit easy, für Gruppe B hard. Conditions[1] ist für
    Gruppe A hard, für Gruppe B easy.
    Zu Beginn des 3D-Taskes soll eine Liste mit den relativen Pfaden (relativ zu Root-Dir des Experimentes)
    zu ALLEN Bildern, die in der jeweiligen Gruppe verwendet werden, in der entsprechenden Reihenfolge 
    erstellt werden. Durch einen Trialindex wird dann innerhalb der Image-Komponente der trial_3D-Routine auf
    das entsprechende Bild zugegriffen, wobei das Bild selbst während der Fixations geladen wird.
'''

if expInfo['group'] == "A":
    first_block = 'Stimuli_3D\\easy'
    second_block = 'Stimuli_3D\\hard'
elif expInfo['group'] == "B":
    first_block = 'Stimuli_3D\\hard'
    second_block = 'Stimuli_3D\\easy'

img_path_1 = exp_root_path + os.sep + first_block     # Pfad der Bilder, die zuerst erscheinen sollen (easy oder hard)
img_path_2 = exp_root_path + os.sep + second_block     # Pfad der Bilder, die als zweites erscheinen sollen

'''
3. Auslesen der Pfade zu den Bilddateien und Erstellen der Liste mit relativen Pfaden, natürlich sortiert

'''

img_files_1 = glob.glob(img_path_1 + os.sep + '*.jpg')  # Erstellt Liste mit Pfaden zu den Bildern, die im 1. Block gezeigt werden
                                                        # (easy oder hard, abhängig von Gruppenzugehörigkeit)
img_files_2 = glob.glob(img_path_2 + os.sep + '*.jpg')  # Liste mit Pfaden zu den Bildern, die im 2. Block gezeigt werden


# Anlegen zweier Listen für relative Pfade. Die Elemente der Listen werden separat natürlich sortiert,
# bevor sie in eine einzelne Liste zusammengeführt werden
img_files_rel_1 = []
img_files_rel_2 = []

# Eigentliches Auslesen der relativen Pfade (Liste der Bilder, die im 1. Block gezeigt werden sollen)
for img in img_files_1:
    img_split = img.split(os.sep)   # trennt die Strings an den Stellen, wo der OS Seperator (Windows: \\) vorliegt
    img_joined = os.sep.join(img_split[-3:])    # fügt die letzten 3 Elemente (Stimuli_3D, easy (oder hard), Filename.jpg zusammen
    img_files_rel_1.append(img_joined)     # fügt den relativen Pfad der img_files_complete-Liste hinzu

# Eigentliches Auslesen der relativen Pfade (Liste der Bilder, die im 2. Block gezeigt werden sollen)
for img in img_files_2:
    img_split = img.split(os.sep)
    img_joined = os.sep.join(img_split[-3:])
    img_files_rel_2.append(img_joined)

# Natural sorting der Listen unter Verwendung der custom Function
img_files_rel_1_sorted = natural_sorted(img_files_rel_1)
img_files_rel_2_sorted = natural_sorted(img_files_rel_2)

# Zusammenführen ("Concatenation") der Listen
# Diese enthält nun alle 2x192 = 384 relativen Pfade zu den Stimuli in der Art, dass
# für Gruppe A zunächst alle Pfade der Bilder im easy-Ordner, dann alle Pfade der Bilder 
# im hard-Ordner folgen. Für Gruppe B verhält es sich entsprechend umgekehrt.
img_files_complete = [*img_files_rel_1_sorted, *img_files_rel_2_sorted]

# Festlegen der Answer-Keys
# Hier können die Tasten, mit denen deckungsgleiche und nicht deckungsgleiche
# Bilder angegeben werden sollen, festgelegt werden. Dies wird bei der
# Bewertung der Antwort (richtig oder falsch) unter End Routine in dieser
# Code Komponenten automatisch berücksichtigt
same_key = 'up'
diff_key = 'down'

# Liste mit erlaubten Keys (die Keyboard-Komponente benötigt die
# erlaubten Keys als Liste. Man kann nicht einfach die Variablennamen
# eintragen)
allowed_keys = [same_key, diff_key]

# Liste mit 0 für korrekte und 1 für falsche Antworten
# Wird unter End Routine dieser Code Komponente verwendet
correct_keys = []
stim_3D = visual.ImageStim(
    win=win,
    name='stim_3D', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(800, 427),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_3D = keyboard.Keyboard()

# Initialize components for Routine "feedback_3D"
feedback_3DClock = core.Clock()
# Festlegen, wie viele der letzten Trials bei Berechnung der korrekten
# Trials für Feedback-Message berücksichtigt werden sollen
# n_Trials_Feedback letzter Trials
# n_Trials_Feedback: Anzahl letzter Trials, die für Berechnung berücksichtigt
# werden sollen
n_Trials_Feedback = 10


feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions_2D"-------
continueRoutine = True
# update component parameters for each repeat
instr_2D_kb.keys = []
instr_2D_kb.rt = []
_instr_2D_kb_allKeys = []
# keep track of which components have finished
instructions_2DComponents = [instr_2D, instr_2D_kb]
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
    
    # *instr_2D_kb* updates
    waitOnFlip = False
    if instr_2D_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2D_kb.frameNStart = frameN  # exact frame index
        instr_2D_kb.tStart = t  # local t and not account for scr refresh
        instr_2D_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2D_kb, 'tStartRefresh')  # time at next scr refresh
        instr_2D_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_2D_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_2D_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_2D_kb.status == STARTED and not waitOnFlip:
        theseKeys = instr_2D_kb.getKeys(keyList=['space'], waitRelease=False)
        _instr_2D_kb_allKeys.extend(theseKeys)
        if len(_instr_2D_kb_allKeys):
            instr_2D_kb.keys = _instr_2D_kb_allKeys[-1].name  # just the last key pressed
            instr_2D_kb.rt = _instr_2D_kb_allKeys[-1].rt
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
if instr_2D_kb.keys in ['', [], None]:  # No response was made
    instr_2D_kb.keys = None
thisExp.addData('instr_2D_kb.keys',instr_2D_kb.keys)
if instr_2D_kb.keys != None:  # we had a response
    thisExp.addData('instr_2D_kb.rt', instr_2D_kb.rt)
thisExp.addData('instr_2D_kb.started', instr_2D_kb.tStartRefresh)
thisExp.addData('instr_2D_kb.stopped', instr_2D_kb.tStopRefresh)
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
    # Logging der Pfade der verwendeten Bilddateien
    # Diese Variablen werden in die Experimental-csv-Daatei geschrieben und
    # als Pfad für die image-Stimuli verwendet
    img_correct_path = 'Stimuli_2d/correct' + str(img_index[trials_2D.thisN]) + '.png' # Pfad des korrekten 2D-Bildes
    img_wrong_path = 'Stimuli_2d/wrong' + str(img_index[trials_2D.thisN]) + '.png' # Pfad des falschen 2D-Bildes
    img_target_path = 'Stimuli_2d/target' + str(img_index[trials_2D.thisN]) + '.png' # Pfad des Target-Bildes
    # keep track of which components have finished
    ITI_Fixation_2DComponents = [fix_point_2D, fix_point_2D_ISI]
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
        
        # *fix_point_2D* updates
        if fix_point_2D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_point_2D.frameNStart = frameN  # exact frame index
            fix_point_2D.tStart = t  # local t and not account for scr refresh
            fix_point_2D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_point_2D, 'tStartRefresh')  # time at next scr refresh
            fix_point_2D.setAutoDraw(True)
        if fix_point_2D.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_point_2D.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_point_2D.tStop = t  # not accounting for scr refresh
                fix_point_2D.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_point_2D, 'tStopRefresh')  # time at next scr refresh
                fix_point_2D.setAutoDraw(False)
        # *fix_point_2D_ISI* period
        if fix_point_2D_ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            fix_point_2D_ISI.frameNStart = frameN  # exact frame index
            fix_point_2D_ISI.tStart = t  # local t and not account for scr refresh
            fix_point_2D_ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_point_2D_ISI, 'tStartRefresh')  # time at next scr refresh
            fix_point_2D_ISI.start(1)
        elif fix_point_2D_ISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *fix_point_2D_ISI*
            img_correct.setImage(img_correct_path)
            img_target.setImage(img_target_path)
            img_wrong.setImage(img_wrong_path)
            # component updates done
            fix_point_2D_ISI.complete()  # finish the static period
            fix_point_2D_ISI.tStop = fix_point_2D_ISI.tStart + 1  # record stop time
        
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
    trials_2D.addData('fix_point_2D.started', fix_point_2D.tStartRefresh)
    trials_2D.addData('fix_point_2D.stopped', fix_point_2D.tStopRefresh)
    trials_2D.addData('fix_point_2D_ISI.started', fix_point_2D_ISI.tStart)
    trials_2D.addData('fix_point_2D_ISI.stopped', fix_point_2D_ISI.tStop)
    
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
                        iter([img_correct, img_wrong])
                        clickableList = [img_correct, img_wrong]
                    except:
                        clickableList = [[img_correct, img_wrong]]
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
    # (in den csv-Dateien kann man anhand der Zahlen
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
    
# completed 15.0 repeats of 'trials_2D'


# ------Prepare to start Routine "instructions_3D"-------
continueRoutine = True
# update component parameters for each repeat
instr_3D_kb.keys = []
instr_3D_kb.rt = []
_instr_3D_kb_allKeys = []
# keep track of which components have finished
instructions_3DComponents = [instr_3D, instr_3D_kb]
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
    
    # *instr_3D* updates
    if instr_3D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3D.frameNStart = frameN  # exact frame index
        instr_3D.tStart = t  # local t and not account for scr refresh
        instr_3D.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3D, 'tStartRefresh')  # time at next scr refresh
        instr_3D.setAutoDraw(True)
    
    # *instr_3D_kb* updates
    waitOnFlip = False
    if instr_3D_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3D_kb.frameNStart = frameN  # exact frame index
        instr_3D_kb.tStart = t  # local t and not account for scr refresh
        instr_3D_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3D_kb, 'tStartRefresh')  # time at next scr refresh
        instr_3D_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_3D_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_3D_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_3D_kb.status == STARTED and not waitOnFlip:
        theseKeys = instr_3D_kb.getKeys(keyList=['space'], waitRelease=False)
        _instr_3D_kb_allKeys.extend(theseKeys)
        if len(_instr_3D_kb_allKeys):
            instr_3D_kb.keys = _instr_3D_kb_allKeys[-1].name  # just the last key pressed
            instr_3D_kb.rt = _instr_3D_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
thisExp.addData('instr_3D.started', instr_3D.tStartRefresh)
thisExp.addData('instr_3D.stopped', instr_3D.tStopRefresh)
# check responses
if instr_3D_kb.keys in ['', [], None]:  # No response was made
    instr_3D_kb.keys = None
thisExp.addData('instr_3D_kb.keys',instr_3D_kb.keys)
if instr_3D_kb.keys != None:  # we had a response
    thisExp.addData('instr_3D_kb.rt', instr_3D_kb.rt)
thisExp.addData('instr_3D_kb.started', instr_3D_kb.tStartRefresh)
thisExp.addData('instr_3D_kb.stopped', instr_3D_kb.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_3D" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3D = data.TrialHandler(nReps=384.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3D')
thisExp.addLoop(trials_3D)  # add the loop to the experiment
thisTrials_3D = trials_3D.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_3D.rgb)
if thisTrials_3D != None:
    for paramName in thisTrials_3D:
        exec('{} = thisTrials_3D[paramName]'.format(paramName))

for thisTrials_3D in trials_3D:
    currentLoop = trials_3D
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_3D.rgb)
    if thisTrials_3D != None:
        for paramName in thisTrials_3D:
            exec('{} = thisTrials_3D[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI_Fixation_3D"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_Fixation_3DComponents = [fix_point_3D, fix_point_3D_ISI]
    for thisComponent in ITI_Fixation_3DComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_Fixation_3DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI_Fixation_3D"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_Fixation_3DClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_Fixation_3DClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_point_3D* updates
        if fix_point_3D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_point_3D.frameNStart = frameN  # exact frame index
            fix_point_3D.tStart = t  # local t and not account for scr refresh
            fix_point_3D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_point_3D, 'tStartRefresh')  # time at next scr refresh
            fix_point_3D.setAutoDraw(True)
        if fix_point_3D.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_point_3D.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_point_3D.tStop = t  # not accounting for scr refresh
                fix_point_3D.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_point_3D, 'tStopRefresh')  # time at next scr refresh
                fix_point_3D.setAutoDraw(False)
        # *fix_point_3D_ISI* period
        if fix_point_3D_ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            fix_point_3D_ISI.frameNStart = frameN  # exact frame index
            fix_point_3D_ISI.tStart = t  # local t and not account for scr refresh
            fix_point_3D_ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_point_3D_ISI, 'tStartRefresh')  # time at next scr refresh
            fix_point_3D_ISI.start(1)
        elif fix_point_3D_ISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *fix_point_3D_ISI*
            stim_3D.setImage(img_files_complete[trials_3D.thisN])
            # component updates done
            fix_point_3D_ISI.complete()  # finish the static period
            fix_point_3D_ISI.tStop = fix_point_3D_ISI.tStart + 1  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_Fixation_3DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_Fixation_3D"-------
    for thisComponent in ITI_Fixation_3DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3D.addData('fix_point_3D.started', fix_point_3D.tStartRefresh)
    trials_3D.addData('fix_point_3D.stopped', fix_point_3D.tStopRefresh)
    trials_3D.addData('fix_point_3D_ISI.started', fix_point_3D_ISI.tStart)
    trials_3D.addData('fix_point_3D_ISI.stopped', fix_point_3D_ISI.tStop)
    
    # ------Prepare to start Routine "trial_3D"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    key_resp_3D.keys = []
    key_resp_3D.rt = []
    _key_resp_3D_allKeys = []
    # keep track of which components have finished
    trial_3DComponents = [stim_3D, key_resp_3D]
    for thisComponent in trial_3DComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_3DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_3D"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_3DClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_3DClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_3D* updates
        if stim_3D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_3D.frameNStart = frameN  # exact frame index
            stim_3D.tStart = t  # local t and not account for scr refresh
            stim_3D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_3D, 'tStartRefresh')  # time at next scr refresh
            stim_3D.setAutoDraw(True)
        if stim_3D.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_3D.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                stim_3D.tStop = t  # not accounting for scr refresh
                stim_3D.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_3D, 'tStopRefresh')  # time at next scr refresh
                stim_3D.setAutoDraw(False)
        
        # *key_resp_3D* updates
        waitOnFlip = False
        if key_resp_3D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3D.frameNStart = frameN  # exact frame index
            key_resp_3D.tStart = t  # local t and not account for scr refresh
            key_resp_3D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3D, 'tStartRefresh')  # time at next scr refresh
            key_resp_3D.status = STARTED
            # AllowedKeys looks like a variable named `allowed_keys`
            if not type(allowed_keys) in [list, tuple, np.ndarray]:
                if not isinstance(allowed_keys, str):
                    logging.error('AllowedKeys variable `allowed_keys` is not string- or list-like.')
                    core.quit()
                elif not ',' in allowed_keys:
                    allowed_keys = (allowed_keys,)
                else:
                    allowed_keys = eval(allowed_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3D.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3D.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3D.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3D.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3D.tStop = t  # not accounting for scr refresh
                key_resp_3D.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3D, 'tStopRefresh')  # time at next scr refresh
                key_resp_3D.status = FINISHED
        if key_resp_3D.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3D.getKeys(keyList=list(allowed_keys), waitRelease=False)
            _key_resp_3D_allKeys.extend(theseKeys)
            if len(_key_resp_3D_allKeys):
                key_resp_3D.keys = _key_resp_3D_allKeys[-1].name  # just the last key pressed
                key_resp_3D.rt = _key_resp_3D_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_3DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_3D"-------
    for thisComponent in trial_3DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    '''
    Überprüfen der Antworttaste der VP auf Richtigkeit.
    Für den Fall, dass die Bilder des 3D Task randomisiert
    bzw. geshuffelt präsentiert werden sollen, erfolgt der
    Check nicht anhand einer Liste mit alternierend up und down
    Einträgen. Stattdessen wird auf ein großes R im relativen
    Pfad des im aktuellen Trial verwendeten Stimulus geprüft.
    Wenn der relative Pfad ein R einhält, handelt es sich um einen
    Trial mit nicht deckungsgleichen Bildern, weshalb dann die
    diff_key-Taste (default: 'down') die korrekte Antwort ist und eine
    1 geloggt wird.
    Wird die same_key-Taste gedrückt, war es eine falsche Antwort und
    es wird die 0 geloggt.
    Umgekehrt verhält es sich mit der Zuordnung in den Trials mit deckungsgleichen
    Stimuli. Hier ist der same_key (default: 'up') die korrekte Antwort,
    weshalb bei Druck dieser Taste eine 1 geloggt wird.
    '''
    
    if "R" in img_files_complete[trials_3D.thisN]:
        if key_resp_3D.keys == diff_key:
            corrAns = 1
        else:
            corrAns = 0
    else:
        if key_resp_3D.keys == same_key:
            corrAns = 1
        else:
            corrAns = 0
    
    # Loggen des relativen Pfades des aktuellen Stimulus
    # sowie der Richtigkeit der Antwort (werden in separate Spalten
    # der Experimental-csv-Datei geschrieben)
    thisExp.addData('corrAns', corrAns)
    thisExp.addData('stim_path', img_files_complete[trials_3D.thisN])
    
    # Loggen der Antworten (diese Liste wird zur Berechnung der Anzahl korrekter Antworten
    # in der feedback_code-Komponente der feedback_3D-Routine verwendet)
    correct_keys.append(corrAns)
    
    # Extraktion des Rotationswinkels des Vergleichsstimulus
    # So kann man später graphisch die Reaktionszeit gegen den Rotationswinkel darstellen.
    # Zunächst wird der relative Pfad des aktuell verwendeten Stimulus (z.B. "Stimuli_3D\easy\07_50.jpg")
    # am Unterstrich "_" getrennt ('Stimuli', '3D\easy\', '50.jpg) und in der Variable
    # splt_path gespeichert.
    # Wenn im Pfad des im akuellen Trial verwendeten Stimulus kein "R" vorkommt (deckungsgleiche Stimuli),
    # wird das letzte Elemente der Liste splt_path (z.B. 50.jpg) am Punkt "." getrennt. 
    # Das vorletzte Element des Resultats (splt_path[-1].split(".")[-2]) ist dann der Rotationswinkel.
    # Wenn ein "R" im relativen Pfad vorkommt, entfällt der letzte Schritt (Split des letzten
    # Elementes der Liste splt_path beim Doppelpunkt und Verwendung des vorletzten Elementes des Resultates).
    # Hier ist das vorletzte Element der Variable splt_path der Rotationswinkel.
    splt_path = img_files_complete[trials_3D.thisN].split("_")
    
    if "R" not in img_files_complete[trials_3D.thisN]:
        rotation_degree = splt_path[-1].split(".")[-2]
        same_or_diff = "same"
    else:
        rotation_degree = splt_path[-2]
        same_or_diff = "diff"
    
    # Fügt den Rotationswinkel des Vergleichsstimulus den Experimentaldaten hinzu
    thisExp.addData('Rotation_Degree', rotation_degree)
    thisExp.addData('Same_or_Diff', same_or_diff)
    
    trials_3D.addData('stim_3D.started', stim_3D.tStartRefresh)
    trials_3D.addData('stim_3D.stopped', stim_3D.tStopRefresh)
    # check responses
    if key_resp_3D.keys in ['', [], None]:  # No response was made
        key_resp_3D.keys = None
    trials_3D.addData('key_resp_3D.keys',key_resp_3D.keys)
    if key_resp_3D.keys != None:  # we had a response
        trials_3D.addData('key_resp_3D.rt', key_resp_3D.rt)
    trials_3D.addData('key_resp_3D.started', key_resp_3D.tStartRefresh)
    trials_3D.addData('key_resp_3D.stopped', key_resp_3D.tStopRefresh)
    
    # ------Prepare to start Routine "feedback_3D"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # Anpassen der Feedback Message nach 10 Trials
    # Falls kein Feedback angezeigt werden soll (da aktueller
    # Trial kein Vielfaches von 10), wird die Routine übersprungen und der 
    # nächste Trial startet. Da Indexing in Python bei 0 beginnt, muss für den
    # Modulo-Operator zum aktuellen Trialindex 1 addiert werden
    if (trials_3D.thisN+1) % n_Trials_Feedback == 0:
        nCorr = sum(correct_keys[-n_Trials_Feedback:])
        msg = str(nCorr) + ' der letzten ' + str(n_Trials_Feedback) + ' korrekt.'
    else:
        msg = ''
        continueRoutine = False
    feedback_text.setText(msg)
    # keep track of which components have finished
    feedback_3DComponents = [feedback_text]
    for thisComponent in feedback_3DComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_3DClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_3D"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback_3DClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_3DClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_3DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_3D"-------
    for thisComponent in feedback_3DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3D.addData('feedback_text.started', feedback_text.tStartRefresh)
    trials_3D.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 384.0 repeats of 'trials_3D'


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
