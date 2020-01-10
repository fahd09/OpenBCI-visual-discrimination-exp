#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Mon Dec 30 21:19:26 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'visual_disc_exp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/fahd/bci/exps/visual_disc_exp/visual_disc_exp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
import time
from pylsl import StreamInfo, StreamOutlet

info = StreamInfo('Ganglion_EEG', 'Markers', 1, 0.0, 'int32','marker')
outlet = StreamOutlet(info)

outlet.push_sample([-1], time.time())
start_text = visual.TextStim(win=win, name='start_text',
    text='Press <up> to begin.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_press = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask='circle',
    ori=1.0, pos=(0, 0), size=.3, sf=sfreq, phase=0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,blendmode='avg',
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "iti"
itiClock = core.Clock()
crosshair = visual.TextStim(win=win, name='crosshair',
    text='+',
    font='Arial',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
finish_text = visual.TextStim(win=win, name='finish_text',
    text='This is the end.\n\nEnd the Marker Streaming now and then press any key to leave.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finish_press = keyboard.Keyboard()

# Initialize components for Routine "finish"
finishClock = core.Clock()
finish_text = visual.TextStim(win=win, name='finish_text',
    text='This is the end.\n\nEnd the Marker Streaming now and then press any key to leave.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finish_press = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
# update component parameters for each repeat
start_press.keys = []
start_press.rt = []
# keep track of which components have finished
startComponents = [start_text, start_press]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        start_text.setAutoDraw(True)
    
    # *start_press* updates
    waitOnFlip = False
    if start_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_press.frameNStart = frameN  # exact frame index
        start_press.tStart = t  # local t and not account for scr refresh
        start_press.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_press, 'tStartRefresh')  # time at next scr refresh
        start_press.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_press.clock.reset)  # t=0 on next screen flip
    if start_press.status == STARTED and not waitOnFlip:
        theseKeys = start_press.getKeys(keyList=['up'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            start_press.keys = theseKeys.name  # just the last key pressed
            start_press.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_press.keys in ['', [], None]:  # No response was made
    start_press.keys = None
thisExp.addData('start_press.keys',start_press.keys)
if start_press.keys != None:  # we had a response
    thisExp.addData('start_press.rt', start_press.rt)
thisExp.addData('start_press.started', start_press.tStartRefresh)
thisExp.addData('start_press.stopped', start_press.tStopRefresh)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ddd = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ddd')
thisExp.addLoop(ddd)  # add the loop to the experiment
thisDdd = ddd.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDdd.rgb)
if thisDdd != None:
    for paramName in thisDdd:
        exec('{} = thisDdd[paramName]'.format(paramName))

for thisDdd in ddd:
    currentLoop = ddd
    # abbreviate parameter names if possible (e.g. rgb = thisDdd.rgb)
    if thisDdd != None:
        for paramName in thisDdd:
            exec('{} = thisDdd[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=10, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('design_ori.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        outlet.push_sample([id], time.time())
        grating.setOpacity(opacity)
        grating.setOri(orientation)
        # keep track of which components have finished
        trialComponents = [grating]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #if frameN<10:
            #    outlet.push_sample([id], time.time())
                # stimulus onsets
            #    outlet.push_sample([id], time.time())
            
            # *grating* updates
            if grating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grating.frameNStart = frameN  # exact frame index
                grating.tStart = t  # local t and not account for scr refresh
                grating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
                grating.setAutoDraw(True)
            if grating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > grating.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    grating.tStop = t  # not accounting for scr refresh
                    grating.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(grating, 'tStopRefresh')  # time at next scr refresh
                    grating.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        outlet.push_sample([-1], time.time())
        #time.sleep(.5)
        trials.addData('grating.started', grating.tStartRefresh)
        trials.addData('grating.stopped', grating.tStopRefresh)
        
        # ------Prepare to start Routine "iti"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        itiComponents = [crosshair]
        for thisComponent in itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "iti"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = itiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=itiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *crosshair* updates
            if crosshair.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crosshair.frameNStart = frameN  # exact frame index
                crosshair.tStart = t  # local t and not account for scr refresh
                crosshair.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crosshair, 'tStartRefresh')  # time at next scr refresh
                crosshair.setAutoDraw(True)
            if crosshair.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crosshair.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    crosshair.tStop = t  # not accounting for scr refresh
                    crosshair.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(crosshair, 'tStopRefresh')  # time at next scr refresh
                    crosshair.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti"-------
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('crosshair.started', crosshair.tStartRefresh)
        trials.addData('crosshair.stopped', crosshair.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials'
    
    
    # ------Prepare to start Routine "finish"-------
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    finish_press.keys = []
    finish_press.rt = []
    # keep track of which components have finished
    finishComponents = [finish_text, finish_press]
    for thisComponent in finishComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "finish"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = finishClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=finishClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *finish_text* updates
        if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_text.frameNStart = frameN  # exact frame index
            finish_text.tStart = t  # local t and not account for scr refresh
            finish_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
            finish_text.setAutoDraw(True)
        if finish_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_text.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                finish_text.tStop = t  # not accounting for scr refresh
                finish_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_text, 'tStopRefresh')  # time at next scr refresh
                finish_text.setAutoDraw(False)
        
        # *finish_press* updates
        waitOnFlip = False
        if finish_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_press.frameNStart = frameN  # exact frame index
            finish_press.tStart = t  # local t and not account for scr refresh
            finish_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_press, 'tStartRefresh')  # time at next scr refresh
            finish_press.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(finish_press.clock.reset)  # t=0 on next screen flip
        if finish_press.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_press.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                finish_press.tStop = t  # not accounting for scr refresh
                finish_press.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_press, 'tStopRefresh')  # time at next scr refresh
                finish_press.status = FINISHED
        if finish_press.status == STARTED and not waitOnFlip:
            theseKeys = finish_press.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                finish_press.keys = theseKeys.name  # just the last key pressed
                finish_press.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finishComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "finish"-------
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ddd.addData('finish_text.started', finish_text.tStartRefresh)
    ddd.addData('finish_text.stopped', finish_text.tStopRefresh)
    # check responses
    if finish_press.keys in ['', [], None]:  # No response was made
        finish_press.keys = None
    ddd.addData('finish_press.keys',finish_press.keys)
    if finish_press.keys != None:  # we had a response
        ddd.addData('finish_press.rt', finish_press.rt)
    ddd.addData('finish_press.started', finish_press.tStartRefresh)
    ddd.addData('finish_press.stopped', finish_press.tStopRefresh)
# completed 1 repeats of 'ddd'


# ------Prepare to start Routine "finish"-------
routineTimer.add(20.000000)
# update component parameters for each repeat
finish_press.keys = []
finish_press.rt = []
# keep track of which components have finished
finishComponents = [finish_text, finish_press]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_text* updates
    if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_text.frameNStart = frameN  # exact frame index
        finish_text.tStart = t  # local t and not account for scr refresh
        finish_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
        finish_text.setAutoDraw(True)
    if finish_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_text.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            finish_text.tStop = t  # not accounting for scr refresh
            finish_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish_text, 'tStopRefresh')  # time at next scr refresh
            finish_text.setAutoDraw(False)
    
    # *finish_press* updates
    waitOnFlip = False
    if finish_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_press.frameNStart = frameN  # exact frame index
        finish_press.tStart = t  # local t and not account for scr refresh
        finish_press.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_press, 'tStartRefresh')  # time at next scr refresh
        finish_press.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finish_press.clock.reset)  # t=0 on next screen flip
    if finish_press.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_press.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            finish_press.tStop = t  # not accounting for scr refresh
            finish_press.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish_press, 'tStopRefresh')  # time at next scr refresh
            finish_press.status = FINISHED
    if finish_press.status == STARTED and not waitOnFlip:
        theseKeys = finish_press.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            finish_press.keys = theseKeys.name  # just the last key pressed
            finish_press.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finish_text.started', finish_text.tStartRefresh)
thisExp.addData('finish_text.stopped', finish_text.tStopRefresh)
# check responses
if finish_press.keys in ['', [], None]:  # No response was made
    finish_press.keys = None
thisExp.addData('finish_press.keys',finish_press.keys)
if finish_press.keys != None:  # we had a response
    thisExp.addData('finish_press.rt', finish_press.rt)
thisExp.addData('finish_press.started', finish_press.tStartRefresh)
thisExp.addData('finish_press.stopped', finish_press.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
