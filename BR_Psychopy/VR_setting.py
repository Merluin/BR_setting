#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Sun Sep 21 15:37:46 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'VR_setting'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1680, 1050]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/thomasquettier/Desktop/BR_setting/VR_setting.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='cm',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'cm'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('blackscreen_kb') is None:
        # initialise blackscreen_kb
        blackscreen_kb = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='blackscreen_kb',
        )
    if deviceManager.getDevice('stim_r_kb') is None:
        # initialise stim_r_kb
        stim_r_kb = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='stim_r_kb',
        )
    if deviceManager.getDevice('stim_l_') is None:
        # initialise stim_l_
        stim_l_ = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='stim_l_',
        )
    if deviceManager.getDevice('both_kb') is None:
        # initialise both_kb
        both_kb = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='both_kb',
        )
    if deviceManager.getDevice('istr_kb') is None:
        # initialise istr_kb
        istr_kb = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='istr_kb',
        )
    if deviceManager.getDevice('trial_kb') is None:
        # initialise trial_kb
        trial_kb = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='trial_kb',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "SETTING" ---
    # Run 'Begin Experiment' code from code_setting
    start_pos = 3
    size_img = 3
    
    rx_pos = start_pos
    lf_pos = start_pos * (-1)
    rx_pos2 = []
    lf_pos2 = []
    
    nb_loop = 1000
    
    # --- Initialize components for Routine "BLACK_SCREEN" ---
    blackscreen_kb = keyboard.Keyboard(deviceName='blackscreen_kb')
    blackscreen_txt = visual.TextStim(win=win, name='blackscreen_txt',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "STIM_R" ---
    stim_r_img = visual.ImageStim(
        win=win,
        name='stim_r_img', 
        image='images/F.png', mask=None, anchor='center',
        ori=0.0, pos=(rx_pos, 0), draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    stim_r_kb = keyboard.Keyboard(deviceName='stim_r_kb')
    
    # --- Initialize components for Routine "BLACK_SCREEN" ---
    blackscreen_kb = keyboard.Keyboard(deviceName='blackscreen_kb')
    blackscreen_txt = visual.TextStim(win=win, name='blackscreen_txt',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "STIM_L" ---
    stim_l_img = visual.ImageStim(
        win=win,
        name='stim_l_img', 
        image='images/F.png', mask=None, anchor='center',
        ori=0.0, pos=(lf_pos, 0), draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    stim_l_ = keyboard.Keyboard(deviceName='stim_l_')
    
    # --- Initialize components for Routine "BLACK_SCREEN" ---
    blackscreen_kb = keyboard.Keyboard(deviceName='blackscreen_kb')
    blackscreen_txt = visual.TextStim(win=win, name='blackscreen_txt',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "both_stim" ---
    both_r_img = visual.ImageStim(
        win=win,
        name='both_r_img', 
        image='images/F.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    both_l_img = visual.ImageStim(
        win=win,
        name='both_l_img', 
        image='images/F.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(3, 3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    both_kb = keyboard.Keyboard(deviceName='both_kb')
    
    # --- Initialize components for Routine "BLACK_SCREEN" ---
    blackscreen_kb = keyboard.Keyboard(deviceName='blackscreen_kb')
    blackscreen_txt = visual.TextStim(win=win, name='blackscreen_txt',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ISTR" ---
    istr_r = visual.ImageStim(
        win=win,
        name='istr_r', 
        image='images/FS.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    istr_l = visual.ImageStim(
        win=win,
        name='istr_l', 
        image='images/FS.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    istr_kb = keyboard.Keyboard(deviceName='istr_kb')
    
    # --- Initialize components for Routine "TRIALS" ---
    trial_l = visual.ImageStim(
        win=win,
        name='trial_l', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    trial_r = visual.ImageStim(
        win=win,
        name='trial_r', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(size_img, size_img),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    trial_kb = keyboard.Keyboard(deviceName='trial_kb')
    trial_txt = visual.TextStim(win=win, name='trial_txt',
        text='Any text\n\nincluding line breaks',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "BLACK_SCREEN" ---
    blackscreen_kb = keyboard.Keyboard(deviceName='blackscreen_kb')
    blackscreen_txt = visual.TextStim(win=win, name='blackscreen_txt',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "SETTING" ---
    # create an object to store info about Routine SETTING
    SETTING = data.Routine(
        name='SETTING',
        components=[],
    )
    SETTING.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for SETTING
    SETTING.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    SETTING.tStart = globalClock.getTime(format='float')
    SETTING.status = STARTED
    thisExp.addData('SETTING.started', SETTING.tStart)
    SETTING.maxDuration = None
    # keep track of which components have finished
    SETTINGComponents = SETTING.components
    for thisComponent in SETTING.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SETTING" ---
    SETTING.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=SETTING,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            SETTING.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SETTING.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SETTING" ---
    for thisComponent in SETTING.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for SETTING
    SETTING.tStop = globalClock.getTime(format='float')
    SETTING.tStopRefresh = tThisFlipGlobal
    thisExp.addData('SETTING.stopped', SETTING.tStop)
    thisExp.nextEntry()
    # the Routine "SETTING" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "BLACK_SCREEN" ---
    # create an object to store info about Routine BLACK_SCREEN
    BLACK_SCREEN = data.Routine(
        name='BLACK_SCREEN',
        components=[blackscreen_kb, blackscreen_txt],
    )
    BLACK_SCREEN.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for blackscreen_kb
    blackscreen_kb.keys = []
    blackscreen_kb.rt = []
    _blackscreen_kb_allKeys = []
    # store start times for BLACK_SCREEN
    BLACK_SCREEN.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    BLACK_SCREEN.tStart = globalClock.getTime(format='float')
    BLACK_SCREEN.status = STARTED
    thisExp.addData('BLACK_SCREEN.started', BLACK_SCREEN.tStart)
    BLACK_SCREEN.maxDuration = None
    # keep track of which components have finished
    BLACK_SCREENComponents = BLACK_SCREEN.components
    for thisComponent in BLACK_SCREEN.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BLACK_SCREEN" ---
    BLACK_SCREEN.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackscreen_kb* updates
        waitOnFlip = False
        
        # if blackscreen_kb is starting this frame...
        if blackscreen_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_kb.frameNStart = frameN  # exact frame index
            blackscreen_kb.tStart = t  # local t and not account for scr refresh
            blackscreen_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(blackscreen_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(blackscreen_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if blackscreen_kb.status == STARTED and not waitOnFlip:
            theseKeys = blackscreen_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _blackscreen_kb_allKeys.extend(theseKeys)
            if len(_blackscreen_kb_allKeys):
                blackscreen_kb.keys = _blackscreen_kb_allKeys[-1].name  # just the last key pressed
                blackscreen_kb.rt = _blackscreen_kb_allKeys[-1].rt
                blackscreen_kb.duration = _blackscreen_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *blackscreen_txt* updates
        
        # if blackscreen_txt is starting this frame...
        if blackscreen_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_txt.frameNStart = frameN  # exact frame index
            blackscreen_txt.tStart = t  # local t and not account for scr refresh
            blackscreen_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_txt.status = STARTED
            blackscreen_txt.setAutoDraw(True)
        
        # if blackscreen_txt is active this frame...
        if blackscreen_txt.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=BLACK_SCREEN,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            BLACK_SCREEN.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BLACK_SCREEN.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BLACK_SCREEN" ---
    for thisComponent in BLACK_SCREEN.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for BLACK_SCREEN
    BLACK_SCREEN.tStop = globalClock.getTime(format='float')
    BLACK_SCREEN.tStopRefresh = tThisFlipGlobal
    thisExp.addData('BLACK_SCREEN.stopped', BLACK_SCREEN.tStop)
    thisExp.nextEntry()
    # the Routine "BLACK_SCREEN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "STIM_R" ---
    # create an object to store info about Routine STIM_R
    STIM_R = data.Routine(
        name='STIM_R',
        components=[stim_r_img, stim_r_kb],
    )
    STIM_R.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for stim_r_kb
    stim_r_kb.keys = []
    stim_r_kb.rt = []
    _stim_r_kb_allKeys = []
    # store start times for STIM_R
    STIM_R.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    STIM_R.tStart = globalClock.getTime(format='float')
    STIM_R.status = STARTED
    thisExp.addData('STIM_R.started', STIM_R.tStart)
    STIM_R.maxDuration = None
    # keep track of which components have finished
    STIM_RComponents = STIM_R.components
    for thisComponent in STIM_R.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "STIM_R" ---
    STIM_R.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_r_img* updates
        
        # if stim_r_img is starting this frame...
        if stim_r_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_r_img.frameNStart = frameN  # exact frame index
            stim_r_img.tStart = t  # local t and not account for scr refresh
            stim_r_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_r_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            stim_r_img.status = STARTED
            stim_r_img.setAutoDraw(True)
        
        # if stim_r_img is active this frame...
        if stim_r_img.status == STARTED:
            # update params
            pass
        
        # *stim_r_kb* updates
        waitOnFlip = False
        
        # if stim_r_kb is starting this frame...
        if stim_r_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_r_kb.frameNStart = frameN  # exact frame index
            stim_r_kb.tStart = t  # local t and not account for scr refresh
            stim_r_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_r_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            stim_r_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stim_r_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stim_r_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stim_r_kb.status == STARTED and not waitOnFlip:
            theseKeys = stim_r_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _stim_r_kb_allKeys.extend(theseKeys)
            if len(_stim_r_kb_allKeys):
                stim_r_kb.keys = _stim_r_kb_allKeys[-1].name  # just the last key pressed
                stim_r_kb.rt = _stim_r_kb_allKeys[-1].rt
                stim_r_kb.duration = _stim_r_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=STIM_R,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            STIM_R.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STIM_R.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "STIM_R" ---
    for thisComponent in STIM_R.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for STIM_R
    STIM_R.tStop = globalClock.getTime(format='float')
    STIM_R.tStopRefresh = tThisFlipGlobal
    thisExp.addData('STIM_R.stopped', STIM_R.tStop)
    thisExp.nextEntry()
    # the Routine "STIM_R" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "BLACK_SCREEN" ---
    # create an object to store info about Routine BLACK_SCREEN
    BLACK_SCREEN = data.Routine(
        name='BLACK_SCREEN',
        components=[blackscreen_kb, blackscreen_txt],
    )
    BLACK_SCREEN.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for blackscreen_kb
    blackscreen_kb.keys = []
    blackscreen_kb.rt = []
    _blackscreen_kb_allKeys = []
    # store start times for BLACK_SCREEN
    BLACK_SCREEN.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    BLACK_SCREEN.tStart = globalClock.getTime(format='float')
    BLACK_SCREEN.status = STARTED
    thisExp.addData('BLACK_SCREEN.started', BLACK_SCREEN.tStart)
    BLACK_SCREEN.maxDuration = None
    # keep track of which components have finished
    BLACK_SCREENComponents = BLACK_SCREEN.components
    for thisComponent in BLACK_SCREEN.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BLACK_SCREEN" ---
    BLACK_SCREEN.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackscreen_kb* updates
        waitOnFlip = False
        
        # if blackscreen_kb is starting this frame...
        if blackscreen_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_kb.frameNStart = frameN  # exact frame index
            blackscreen_kb.tStart = t  # local t and not account for scr refresh
            blackscreen_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(blackscreen_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(blackscreen_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if blackscreen_kb.status == STARTED and not waitOnFlip:
            theseKeys = blackscreen_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _blackscreen_kb_allKeys.extend(theseKeys)
            if len(_blackscreen_kb_allKeys):
                blackscreen_kb.keys = _blackscreen_kb_allKeys[-1].name  # just the last key pressed
                blackscreen_kb.rt = _blackscreen_kb_allKeys[-1].rt
                blackscreen_kb.duration = _blackscreen_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *blackscreen_txt* updates
        
        # if blackscreen_txt is starting this frame...
        if blackscreen_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_txt.frameNStart = frameN  # exact frame index
            blackscreen_txt.tStart = t  # local t and not account for scr refresh
            blackscreen_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_txt.status = STARTED
            blackscreen_txt.setAutoDraw(True)
        
        # if blackscreen_txt is active this frame...
        if blackscreen_txt.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=BLACK_SCREEN,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            BLACK_SCREEN.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BLACK_SCREEN.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BLACK_SCREEN" ---
    for thisComponent in BLACK_SCREEN.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for BLACK_SCREEN
    BLACK_SCREEN.tStop = globalClock.getTime(format='float')
    BLACK_SCREEN.tStopRefresh = tThisFlipGlobal
    thisExp.addData('BLACK_SCREEN.stopped', BLACK_SCREEN.tStop)
    thisExp.nextEntry()
    # the Routine "BLACK_SCREEN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "STIM_L" ---
    # create an object to store info about Routine STIM_L
    STIM_L = data.Routine(
        name='STIM_L',
        components=[stim_l_img, stim_l_],
    )
    STIM_L.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for stim_l_
    stim_l_.keys = []
    stim_l_.rt = []
    _stim_l__allKeys = []
    # store start times for STIM_L
    STIM_L.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    STIM_L.tStart = globalClock.getTime(format='float')
    STIM_L.status = STARTED
    thisExp.addData('STIM_L.started', STIM_L.tStart)
    STIM_L.maxDuration = None
    # keep track of which components have finished
    STIM_LComponents = STIM_L.components
    for thisComponent in STIM_L.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "STIM_L" ---
    STIM_L.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_l_img* updates
        
        # if stim_l_img is starting this frame...
        if stim_l_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_l_img.frameNStart = frameN  # exact frame index
            stim_l_img.tStart = t  # local t and not account for scr refresh
            stim_l_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_l_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            stim_l_img.status = STARTED
            stim_l_img.setAutoDraw(True)
        
        # if stim_l_img is active this frame...
        if stim_l_img.status == STARTED:
            # update params
            pass
        
        # *stim_l_* updates
        waitOnFlip = False
        
        # if stim_l_ is starting this frame...
        if stim_l_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_l_.frameNStart = frameN  # exact frame index
            stim_l_.tStart = t  # local t and not account for scr refresh
            stim_l_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_l_, 'tStartRefresh')  # time at next scr refresh
            # update status
            stim_l_.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stim_l_.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stim_l_.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stim_l_.status == STARTED and not waitOnFlip:
            theseKeys = stim_l_.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _stim_l__allKeys.extend(theseKeys)
            if len(_stim_l__allKeys):
                stim_l_.keys = _stim_l__allKeys[-1].name  # just the last key pressed
                stim_l_.rt = _stim_l__allKeys[-1].rt
                stim_l_.duration = _stim_l__allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=STIM_L,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            STIM_L.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in STIM_L.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "STIM_L" ---
    for thisComponent in STIM_L.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for STIM_L
    STIM_L.tStop = globalClock.getTime(format='float')
    STIM_L.tStopRefresh = tThisFlipGlobal
    thisExp.addData('STIM_L.stopped', STIM_L.tStop)
    thisExp.nextEntry()
    # the Routine "STIM_L" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "BLACK_SCREEN" ---
    # create an object to store info about Routine BLACK_SCREEN
    BLACK_SCREEN = data.Routine(
        name='BLACK_SCREEN',
        components=[blackscreen_kb, blackscreen_txt],
    )
    BLACK_SCREEN.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for blackscreen_kb
    blackscreen_kb.keys = []
    blackscreen_kb.rt = []
    _blackscreen_kb_allKeys = []
    # store start times for BLACK_SCREEN
    BLACK_SCREEN.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    BLACK_SCREEN.tStart = globalClock.getTime(format='float')
    BLACK_SCREEN.status = STARTED
    thisExp.addData('BLACK_SCREEN.started', BLACK_SCREEN.tStart)
    BLACK_SCREEN.maxDuration = None
    # keep track of which components have finished
    BLACK_SCREENComponents = BLACK_SCREEN.components
    for thisComponent in BLACK_SCREEN.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BLACK_SCREEN" ---
    BLACK_SCREEN.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackscreen_kb* updates
        waitOnFlip = False
        
        # if blackscreen_kb is starting this frame...
        if blackscreen_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_kb.frameNStart = frameN  # exact frame index
            blackscreen_kb.tStart = t  # local t and not account for scr refresh
            blackscreen_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(blackscreen_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(blackscreen_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if blackscreen_kb.status == STARTED and not waitOnFlip:
            theseKeys = blackscreen_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _blackscreen_kb_allKeys.extend(theseKeys)
            if len(_blackscreen_kb_allKeys):
                blackscreen_kb.keys = _blackscreen_kb_allKeys[-1].name  # just the last key pressed
                blackscreen_kb.rt = _blackscreen_kb_allKeys[-1].rt
                blackscreen_kb.duration = _blackscreen_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *blackscreen_txt* updates
        
        # if blackscreen_txt is starting this frame...
        if blackscreen_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_txt.frameNStart = frameN  # exact frame index
            blackscreen_txt.tStart = t  # local t and not account for scr refresh
            blackscreen_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_txt.status = STARTED
            blackscreen_txt.setAutoDraw(True)
        
        # if blackscreen_txt is active this frame...
        if blackscreen_txt.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=BLACK_SCREEN,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            BLACK_SCREEN.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BLACK_SCREEN.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BLACK_SCREEN" ---
    for thisComponent in BLACK_SCREEN.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for BLACK_SCREEN
    BLACK_SCREEN.tStop = globalClock.getTime(format='float')
    BLACK_SCREEN.tStopRefresh = tThisFlipGlobal
    thisExp.addData('BLACK_SCREEN.stopped', BLACK_SCREEN.tStop)
    thisExp.nextEntry()
    # the Routine "BLACK_SCREEN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Loop_setting = data.TrialHandler2(
        name='Loop_setting',
        nReps=nb_loop, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('condition.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(Loop_setting)  # add the loop to the experiment
    thisLoop_setting = Loop_setting.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_setting.rgb)
    if thisLoop_setting != None:
        for paramName in thisLoop_setting:
            globals()[paramName] = thisLoop_setting[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_setting in Loop_setting:
        Loop_setting.status = STARTED
        if hasattr(thisLoop_setting, 'status'):
            thisLoop_setting.status = STARTED
        currentLoop = Loop_setting
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_setting.rgb)
        if thisLoop_setting != None:
            for paramName in thisLoop_setting:
                globals()[paramName] = thisLoop_setting[paramName]
        
        # --- Prepare to start Routine "both_stim" ---
        # create an object to store info about Routine both_stim
        both_stim = data.Routine(
            name='both_stim',
            components=[both_r_img, both_l_img, both_kb],
        )
        both_stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        both_r_img.setPos((rx_pos, 0))
        both_l_img.setPos((lf_pos, 0))
        # create starting attributes for both_kb
        both_kb.keys = []
        both_kb.rt = []
        _both_kb_allKeys = []
        # store start times for both_stim
        both_stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        both_stim.tStart = globalClock.getTime(format='float')
        both_stim.status = STARTED
        thisExp.addData('both_stim.started', both_stim.tStart)
        both_stim.maxDuration = None
        # keep track of which components have finished
        both_stimComponents = both_stim.components
        for thisComponent in both_stim.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "both_stim" ---
        both_stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_setting, 'status') and thisLoop_setting.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *both_r_img* updates
            
            # if both_r_img is starting this frame...
            if both_r_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                both_r_img.frameNStart = frameN  # exact frame index
                both_r_img.tStart = t  # local t and not account for scr refresh
                both_r_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(both_r_img, 'tStartRefresh')  # time at next scr refresh
                # update status
                both_r_img.status = STARTED
                both_r_img.setAutoDraw(True)
            
            # if both_r_img is active this frame...
            if both_r_img.status == STARTED:
                # update params
                pass
            
            # *both_l_img* updates
            
            # if both_l_img is starting this frame...
            if both_l_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                both_l_img.frameNStart = frameN  # exact frame index
                both_l_img.tStart = t  # local t and not account for scr refresh
                both_l_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(both_l_img, 'tStartRefresh')  # time at next scr refresh
                # update status
                both_l_img.status = STARTED
                both_l_img.setAutoDraw(True)
            
            # if both_l_img is active this frame...
            if both_l_img.status == STARTED:
                # update params
                pass
            
            # *both_kb* updates
            waitOnFlip = False
            
            # if both_kb is starting this frame...
            if both_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                both_kb.frameNStart = frameN  # exact frame index
                both_kb.tStart = t  # local t and not account for scr refresh
                both_kb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(both_kb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'both_kb.started')
                # update status
                both_kb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(both_kb.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(both_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if both_kb.status == STARTED and not waitOnFlip:
                theseKeys = both_kb.getKeys(keyList=['up','down','space'], ignoreKeys=["escape"], waitRelease=False)
                _both_kb_allKeys.extend(theseKeys)
                if len(_both_kb_allKeys):
                    both_kb.keys = _both_kb_allKeys[-1].name  # just the last key pressed
                    both_kb.rt = _both_kb_allKeys[-1].rt
                    both_kb.duration = _both_kb_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=both_stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                both_stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in both_stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "both_stim" ---
        for thisComponent in both_stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for both_stim
        both_stim.tStop = globalClock.getTime(format='float')
        both_stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('both_stim.stopped', both_stim.tStop)
        # Run 'End Routine' code from both_code
        key = both_kb.keys
        
        if key == 'space':
            level = 0
            Loop_setting.finished=True
        elif key == 'up':
            level = .2
        elif key == 'down':
            level = -.2
            
        rx_pos = rx_pos + level
        lf_pos = lf_pos + (level*-1)
        
        
        thisExp.addData("position.left", lf_pos)
        thisExp.addData("position.right", rx_pos)
        # the Routine "both_stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLoop_setting as finished
        if hasattr(thisLoop_setting, 'status'):
            thisLoop_setting.status = FINISHED
        # if awaiting a pause, pause now
        if Loop_setting.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Loop_setting.status = STARTED
        thisExp.nextEntry()
        
    # completed nb_loop repeats of 'Loop_setting'
    Loop_setting.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "BLACK_SCREEN" ---
    # create an object to store info about Routine BLACK_SCREEN
    BLACK_SCREEN = data.Routine(
        name='BLACK_SCREEN',
        components=[blackscreen_kb, blackscreen_txt],
    )
    BLACK_SCREEN.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for blackscreen_kb
    blackscreen_kb.keys = []
    blackscreen_kb.rt = []
    _blackscreen_kb_allKeys = []
    # store start times for BLACK_SCREEN
    BLACK_SCREEN.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    BLACK_SCREEN.tStart = globalClock.getTime(format='float')
    BLACK_SCREEN.status = STARTED
    thisExp.addData('BLACK_SCREEN.started', BLACK_SCREEN.tStart)
    BLACK_SCREEN.maxDuration = None
    # keep track of which components have finished
    BLACK_SCREENComponents = BLACK_SCREEN.components
    for thisComponent in BLACK_SCREEN.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BLACK_SCREEN" ---
    BLACK_SCREEN.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackscreen_kb* updates
        waitOnFlip = False
        
        # if blackscreen_kb is starting this frame...
        if blackscreen_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_kb.frameNStart = frameN  # exact frame index
            blackscreen_kb.tStart = t  # local t and not account for scr refresh
            blackscreen_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(blackscreen_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(blackscreen_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if blackscreen_kb.status == STARTED and not waitOnFlip:
            theseKeys = blackscreen_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _blackscreen_kb_allKeys.extend(theseKeys)
            if len(_blackscreen_kb_allKeys):
                blackscreen_kb.keys = _blackscreen_kb_allKeys[-1].name  # just the last key pressed
                blackscreen_kb.rt = _blackscreen_kb_allKeys[-1].rt
                blackscreen_kb.duration = _blackscreen_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *blackscreen_txt* updates
        
        # if blackscreen_txt is starting this frame...
        if blackscreen_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_txt.frameNStart = frameN  # exact frame index
            blackscreen_txt.tStart = t  # local t and not account for scr refresh
            blackscreen_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_txt.status = STARTED
            blackscreen_txt.setAutoDraw(True)
        
        # if blackscreen_txt is active this frame...
        if blackscreen_txt.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=BLACK_SCREEN,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            BLACK_SCREEN.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BLACK_SCREEN.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BLACK_SCREEN" ---
    for thisComponent in BLACK_SCREEN.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for BLACK_SCREEN
    BLACK_SCREEN.tStop = globalClock.getTime(format='float')
    BLACK_SCREEN.tStopRefresh = tThisFlipGlobal
    thisExp.addData('BLACK_SCREEN.stopped', BLACK_SCREEN.tStop)
    thisExp.nextEntry()
    # the Routine "BLACK_SCREEN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISTR" ---
    # create an object to store info about Routine ISTR
    ISTR = data.Routine(
        name='ISTR',
        components=[istr_r, istr_l, istr_kb],
    )
    ISTR.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    istr_r.setPos((rx_pos, 0))
    istr_l.setPos((lf_pos, 0))
    # create starting attributes for istr_kb
    istr_kb.keys = []
    istr_kb.rt = []
    _istr_kb_allKeys = []
    # store start times for ISTR
    ISTR.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISTR.tStart = globalClock.getTime(format='float')
    ISTR.status = STARTED
    thisExp.addData('ISTR.started', ISTR.tStart)
    ISTR.maxDuration = None
    # keep track of which components have finished
    ISTRComponents = ISTR.components
    for thisComponent in ISTR.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISTR" ---
    ISTR.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *istr_r* updates
        
        # if istr_r is starting this frame...
        if istr_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            istr_r.frameNStart = frameN  # exact frame index
            istr_r.tStart = t  # local t and not account for scr refresh
            istr_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_r, 'tStartRefresh')  # time at next scr refresh
            # update status
            istr_r.status = STARTED
            istr_r.setAutoDraw(True)
        
        # if istr_r is active this frame...
        if istr_r.status == STARTED:
            # update params
            pass
        
        # *istr_l* updates
        
        # if istr_l is starting this frame...
        if istr_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            istr_l.frameNStart = frameN  # exact frame index
            istr_l.tStart = t  # local t and not account for scr refresh
            istr_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_l, 'tStartRefresh')  # time at next scr refresh
            # update status
            istr_l.status = STARTED
            istr_l.setAutoDraw(True)
        
        # if istr_l is active this frame...
        if istr_l.status == STARTED:
            # update params
            pass
        
        # *istr_kb* updates
        waitOnFlip = False
        
        # if istr_kb is starting this frame...
        if istr_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            istr_kb.frameNStart = frameN  # exact frame index
            istr_kb.tStart = t  # local t and not account for scr refresh
            istr_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(istr_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            istr_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(istr_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(istr_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if istr_kb.status == STARTED and not waitOnFlip:
            theseKeys = istr_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _istr_kb_allKeys.extend(theseKeys)
            if len(_istr_kb_allKeys):
                istr_kb.keys = _istr_kb_allKeys[-1].name  # just the last key pressed
                istr_kb.rt = _istr_kb_allKeys[-1].rt
                istr_kb.duration = _istr_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ISTR,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISTR.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISTR.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISTR" ---
    for thisComponent in ISTR.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISTR
    ISTR.tStop = globalClock.getTime(format='float')
    ISTR.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISTR.stopped', ISTR.tStop)
    thisExp.nextEntry()
    # the Routine "ISTR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Loop_trial = data.TrialHandler2(
        name='Loop_trial',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('condition.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(Loop_trial)  # add the loop to the experiment
    thisLoop_trial = Loop_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial:
            globals()[paramName] = thisLoop_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_trial in Loop_trial:
        Loop_trial.status = STARTED
        if hasattr(thisLoop_trial, 'status'):
            thisLoop_trial.status = STARTED
        currentLoop = Loop_trial
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
        if thisLoop_trial != None:
            for paramName in thisLoop_trial:
                globals()[paramName] = thisLoop_trial[paramName]
        
        # --- Prepare to start Routine "TRIALS" ---
        # create an object to store info about Routine TRIALS
        TRIALS = data.Routine(
            name='TRIALS',
            components=[trial_l, trial_r, trial_kb, trial_txt],
        )
        TRIALS.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        trial_l.setPos((lf_pos, 0))
        trial_l.setImage(stim_left)
        trial_r.setPos((rx_pos, 0))
        trial_r.setImage(stim_right)
        # create starting attributes for trial_kb
        trial_kb.keys = []
        trial_kb.rt = []
        _trial_kb_allKeys = []
        # store start times for TRIALS
        TRIALS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TRIALS.tStart = globalClock.getTime(format='float')
        TRIALS.status = STARTED
        thisExp.addData('TRIALS.started', TRIALS.tStart)
        TRIALS.maxDuration = None
        # keep track of which components have finished
        TRIALSComponents = TRIALS.components
        for thisComponent in TRIALS.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TRIALS" ---
        TRIALS.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 32.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_trial, 'status') and thisLoop_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_l* updates
            
            # if trial_l is starting this frame...
            if trial_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_l.frameNStart = frameN  # exact frame index
                trial_l.tStart = t  # local t and not account for scr refresh
                trial_l.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_l, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_l.started')
                # update status
                trial_l.status = STARTED
                trial_l.setAutoDraw(True)
            
            # if trial_l is active this frame...
            if trial_l.status == STARTED:
                # update params
                pass
            
            # if trial_l is stopping this frame...
            if trial_l.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_l.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_l.tStop = t  # not accounting for scr refresh
                    trial_l.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_l.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_l.stopped')
                    # update status
                    trial_l.status = FINISHED
                    trial_l.setAutoDraw(False)
            
            # *trial_r* updates
            
            # if trial_r is starting this frame...
            if trial_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_r.frameNStart = frameN  # exact frame index
                trial_r.tStart = t  # local t and not account for scr refresh
                trial_r.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_r, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_r.started')
                # update status
                trial_r.status = STARTED
                trial_r.setAutoDraw(True)
            
            # if trial_r is active this frame...
            if trial_r.status == STARTED:
                # update params
                pass
            
            # if trial_r is stopping this frame...
            if trial_r.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_r.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_r.tStop = t  # not accounting for scr refresh
                    trial_r.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_r.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_r.stopped')
                    # update status
                    trial_r.status = FINISHED
                    trial_r.setAutoDraw(False)
            
            # *trial_kb* updates
            waitOnFlip = False
            
            # if trial_kb is starting this frame...
            if trial_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_kb.frameNStart = frameN  # exact frame index
                trial_kb.tStart = t  # local t and not account for scr refresh
                trial_kb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_kb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_kb.started')
                # update status
                trial_kb.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trial_kb.clock.reset)  # t=0 on next screen flip
            
            # if trial_kb is stopping this frame...
            if trial_kb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_kb.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_kb.tStop = t  # not accounting for scr refresh
                    trial_kb.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_kb.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_kb.stopped')
                    # update status
                    trial_kb.status = FINISHED
                    trial_kb.status = FINISHED
            if trial_kb.status == STARTED and not waitOnFlip:
                theseKeys = trial_kb.getKeys(keyList=['j','k','l'], ignoreKeys=["escape"], waitRelease=False)
                _trial_kb_allKeys.extend(theseKeys)
                if len(_trial_kb_allKeys):
                    trial_kb.keys = [key.name for key in _trial_kb_allKeys]  # storing all keys
                    trial_kb.rt = [key.rt for key in _trial_kb_allKeys]
                    trial_kb.duration = [key.duration for key in _trial_kb_allKeys]
            
            # *trial_txt* updates
            
            # if trial_txt is starting this frame...
            if trial_txt.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
                # keep track of start time/frame for later
                trial_txt.frameNStart = frameN  # exact frame index
                trial_txt.tStart = t  # local t and not account for scr refresh
                trial_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_txt.started')
                # update status
                trial_txt.status = STARTED
                trial_txt.setAutoDraw(True)
            
            # if trial_txt is active this frame...
            if trial_txt.status == STARTED:
                # update params
                pass
            
            # if trial_txt is stopping this frame...
            if trial_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_txt.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_txt.tStop = t  # not accounting for scr refresh
                    trial_txt.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_txt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_txt.stopped')
                    # update status
                    trial_txt.status = FINISHED
                    trial_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=TRIALS,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                TRIALS.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TRIALS.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TRIALS" ---
        for thisComponent in TRIALS.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TRIALS
        TRIALS.tStop = globalClock.getTime(format='float')
        TRIALS.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TRIALS.stopped', TRIALS.tStop)
        # check responses
        if trial_kb.keys in ['', [], None]:  # No response was made
            trial_kb.keys = None
        Loop_trial.addData('trial_kb.keys',trial_kb.keys)
        if trial_kb.keys != None:  # we had a response
            Loop_trial.addData('trial_kb.rt', trial_kb.rt)
            Loop_trial.addData('trial_kb.duration', trial_kb.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if TRIALS.maxDurationReached:
            routineTimer.addTime(-TRIALS.maxDuration)
        elif TRIALS.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-32.000000)
        # mark thisLoop_trial as finished
        if hasattr(thisLoop_trial, 'status'):
            thisLoop_trial.status = FINISHED
        # if awaiting a pause, pause now
        if Loop_trial.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Loop_trial.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Loop_trial'
    Loop_trial.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "BLACK_SCREEN" ---
    # create an object to store info about Routine BLACK_SCREEN
    BLACK_SCREEN = data.Routine(
        name='BLACK_SCREEN',
        components=[blackscreen_kb, blackscreen_txt],
    )
    BLACK_SCREEN.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for blackscreen_kb
    blackscreen_kb.keys = []
    blackscreen_kb.rt = []
    _blackscreen_kb_allKeys = []
    # store start times for BLACK_SCREEN
    BLACK_SCREEN.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    BLACK_SCREEN.tStart = globalClock.getTime(format='float')
    BLACK_SCREEN.status = STARTED
    thisExp.addData('BLACK_SCREEN.started', BLACK_SCREEN.tStart)
    BLACK_SCREEN.maxDuration = None
    # keep track of which components have finished
    BLACK_SCREENComponents = BLACK_SCREEN.components
    for thisComponent in BLACK_SCREEN.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BLACK_SCREEN" ---
    BLACK_SCREEN.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blackscreen_kb* updates
        waitOnFlip = False
        
        # if blackscreen_kb is starting this frame...
        if blackscreen_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_kb.frameNStart = frameN  # exact frame index
            blackscreen_kb.tStart = t  # local t and not account for scr refresh
            blackscreen_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_kb, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(blackscreen_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(blackscreen_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if blackscreen_kb.status == STARTED and not waitOnFlip:
            theseKeys = blackscreen_kb.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _blackscreen_kb_allKeys.extend(theseKeys)
            if len(_blackscreen_kb_allKeys):
                blackscreen_kb.keys = _blackscreen_kb_allKeys[-1].name  # just the last key pressed
                blackscreen_kb.rt = _blackscreen_kb_allKeys[-1].rt
                blackscreen_kb.duration = _blackscreen_kb_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *blackscreen_txt* updates
        
        # if blackscreen_txt is starting this frame...
        if blackscreen_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blackscreen_txt.frameNStart = frameN  # exact frame index
            blackscreen_txt.tStart = t  # local t and not account for scr refresh
            blackscreen_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blackscreen_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            blackscreen_txt.status = STARTED
            blackscreen_txt.setAutoDraw(True)
        
        # if blackscreen_txt is active this frame...
        if blackscreen_txt.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=BLACK_SCREEN,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            BLACK_SCREEN.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BLACK_SCREEN.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BLACK_SCREEN" ---
    for thisComponent in BLACK_SCREEN.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for BLACK_SCREEN
    BLACK_SCREEN.tStop = globalClock.getTime(format='float')
    BLACK_SCREEN.tStopRefresh = tThisFlipGlobal
    thisExp.addData('BLACK_SCREEN.stopped', BLACK_SCREEN.tStop)
    thisExp.nextEntry()
    # the Routine "BLACK_SCREEN" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
