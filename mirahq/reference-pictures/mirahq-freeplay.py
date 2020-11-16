import pyautogui
import os
from time import sleep

def getAllTasks():
    pyautogui.keyDown('d')
    sleep(0.01)
    pyautogui.keyUp('d')
    pyautogui.press('space')
    sleep(0.2)
    adminFolder = pyautogui.locateCenterOnScreen('reference-pictures/Task Tester 2000 Admin.png')
    pyautogui.click(adminFolder)
    pyautogui.click
    
pyautogui.keyDown('w')
sleep(0.8)
pyautogui.keyUp('w')
pyautogui.press('space')
sleep(0.3)

def cafeteriaEmptyGarbage():
    sleep(0.05)
    handle = pyautogui.locateCenterOnScreen('reference-pictures/Cafeteria Empty Garbage Handle.png')
    pyautogui.moveTo(handle)
    pyautogui.mouseDown(button='left')
    end = pyautogui.locateCenterOnScreen('reference-pictures/Cafeteria Empty Garbage End.png')
    pyautogui.moveTo(end)
    sleep(1.4)
    pyautogui.mouseUp(button='left')

cafeteriaEmptyGarbage()
sleep(1)
pyautogui.keyDown('d')
sleep(0.8)
pyautogui.keyUp('d')
pyautogui.press('space')
sleep(0.2)

def cafeteriaBuyBeverage():
    pyautogui.press('esc')

cafeteriaBuyBeverage()

pyautogui.keyDown('a')
sleep(2)
pyautogui.keyUp('a')
pyautogui.keyDown('s')
sleep(1.75)
pyautogui.keyUp('s')
pyautogui.keyDown('a')
sleep(1.2)
pyautogui.keyUp('a')
pyautogui.press('space')

def wiresTask():
    yellowWireStart1 = pyautogui.locateOnScreen('reference-pictures/Yellow Wire Start1.png')
    yellowWireStart2 = pyautogui.locateOnScreen('reference-pictures/Yellow Wire Start2.png')
    yellowWireStart3 = pyautogui.locateOnScreen('reference-pictures/Yellow Wire Start3.png')
    yellowWireStart4 = pyautogui.locateOnScreen('reference-pictures/Yellow Wire Start4.png')
    yellowWireEnd = pyautogui.locateOnScreen('reference-pictures/Yellow Wire End.png')
    pyautogui.moveTo(yellowWireStart1)
    pyautogui.moveTo(yellowWireStart2)
    pyautogui.moveTo(yellowWireStart3)
    pyautogui.moveTo(yellowWireStart4)
    pyautogui.mouseDown(button='left')
    sleep(0.05)
    pyautogui.moveTo(yellowWireEnd)
    sleep(0.01)
    pyautogui.mouseUp(button='left')

    blueWireStart1 = pyautogui.locateOnScreen('reference-pictures/Blue Wire Start1.png')
    blueWireStart2 = pyautogui.locateOnScreen('reference-pictures/Blue Wire Start2.png')
    blueWireStart3 = pyautogui.locateOnScreen('reference-pictures/Blue Wire Start3.png')
    blueWireStart4 = pyautogui.locateOnScreen('reference-pictures/Blue Wire Start4.png')
    blueWireEnd = pyautogui.locateOnScreen('reference-pictures/Blue Wire End.png')
    pyautogui.moveTo(blueWireStart1)
    pyautogui.moveTo(blueWireStart2)
    pyautogui.moveTo(blueWireStart3)
    pyautogui.moveTo(blueWireStart4)
    pyautogui.mouseDown(button='left')
    sleep(0.05)
    pyautogui.moveTo(blueWireEnd)
    sleep(0.01)
    pyautogui.mouseUp(button='left')

    redWireStart1 = pyautogui.locateOnScreen('reference-pictures/Red Wire Start1.png')
    redWireStart2 = pyautogui.locateOnScreen('reference-pictures/Red Wire Start2.png')
    redWireStart3 = pyautogui.locateOnScreen('reference-pictures/Red Wire Start3.png')
    redWireStart4 = pyautogui.locateOnScreen('reference-pictures/Red Wire Start4.png')
    redWireEnd = pyautogui.locateOnScreen('reference-pictures/Red Wire End.png')
    pyautogui.moveTo(redWireStart1)
    pyautogui.moveTo(redWireStart2)
    pyautogui.moveTo(redWireStart3)
    pyautogui.moveTo(redWireStart4)
    pyautogui.mouseDown(button='left')
    sleep(0.05)
    pyautogui.moveTo(redWireEnd)
    sleep(0.01)
    pyautogui.mouseUp(button='left')

    pinkWireStart1 = pyautogui.locateOnScreen('reference-pictures/Pink Wire Start1.png')
    pinkWireStart2 = pyautogui.locateOnScreen('reference-pictures/Pink Wire Start2.png')
    pinkWireStart3 = pyautogui.locateOnScreen('reference-pictures/Pink Wire Start3.png')
    pinkWireStart4 = pyautogui.locateOnScreen('reference-pictures/Pink Wire Start4.png')
    pinkWireEnd = pyautogui.locateOnScreen('reference-pictures/Pink Wire End.png')
    pyautogui.moveTo(pinkWireStart1)
    pyautogui.moveTo(pinkWireStart2)
    pyautogui.moveTo(pinkWireStart3)
    pyautogui.moveTo(pinkWireStart4)
    pyautogui.mouseDown(button='left')
    sleep(0.05)
    pyautogui.moveTo(pinkWireEnd)
    sleep(0.01)
    pyautogui.mouseUp(button='left')
    
sleep(0.2)
wiresTask()
sleep(0.2)
pyautogui.keyDown('d')
sleep(0.2)
pyautogui.keyUp('d')
pyautogui.keyDown('w')
sleep(0.4)
pyautogui.keyUp('w')
pyautogui.keyDown('a')
sleep(0.3)
pyautogui.keyUp('a')
pyautogui.keyDown('w')
sleep(0.8)
pyautogui.keyUp('w')
pyautogui.keyDown('d')
sleep(0.4)
pyautogui.keyUp('d')
pyautogui.keyDown('w')
sleep(0.2)
pyautogui.keyUp('w')
pyautogui.press('space')
sleep(0.2)

def wateringCan():    
    can1 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can1.png')
    can2 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can2.png')
    can3 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can3.png')
    can4 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can4.png')
    can5 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can5.png')
    can6 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can6.png')
    can7 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can7.png')
    can8 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can8.png')
    can9 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can9.png')
    can10 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can10.png')
    can11 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can11.png')
    can12 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can12.png')
    can13 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can13.png')
    can14 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can14.png')
    can15 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can15.png')
    can16 = pyautogui.locateCenterOnScreen('reference-pictures/Watering Can16.png')

    if (pyautogui.locateOnScreen('reference-pictures/Watering Can1.png') is not None):
        pyautogui.click(can1)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can2.png') is not None):
        pyautogui.click(can2)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can3.png') is not None):
        pyautogui.click(can3)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can4.png') is not None):
        pyautogui.click(can4)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can5.png') is not None):
        pyautogui.click(can5)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can6.png') is not None):
        pyautogui.click(can6)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can7.png') is not None):
        pyautogui.click(can7)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can8.png') is not None):
        pyautogui.click(can8)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can9.png') is not None):
        pyautogui.click(can9)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can10.png') is not None):
        pyautogui.click(can10)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can11.png') is not None):
        pyautogui.click(can11)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can12.png') is not None):
        pyautogui.click(can12)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can13.png') is not None):
        pyautogui.click(can13)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can14.png') is not None):
        pyautogui.click(can14)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can15.png') is not None):
        pyautogui.click(can15)
    if (pyautogui.locateOnScreen('reference-pictures/Watering Can16.png') is not None):
        pyautogui.click(can16)

wateringCan()
sleep(0.2)
pyautogui.keyDown('s')
sleep(0.2)
pyautogui.keyUp('s')
pyautogui.keyDown('a')
sleep(0.4)
pyautogui.keyUp('a')
pyautogui.keyDown('s')
sleep(0.6)
pyautogui.keyUp('s')
pyautogui.keyDown('d')
sleep(0.4)
pyautogui.keyUp('d')
pyautogui.keyDown('s')
sleep(1)
pyautogui.keyUp('s')
pyautogui.keyDown('d')
sleep(0.6)
pyautogui.keyUp('d')
pyautogui.keyDown('s')
sleep(0.5)
pyautogui.keyUp('s')
pyautogui.keyDown('d')
sleep(2.6)
pyautogui.keyUp('d')
pyautogui.press('space')
sleep(0.2)

def weatherDataMeasure():
    begin = pyautogui.locateCenterOnScreen('reference-pictures/Weather Data Measure.png')
    pyautogui.click(begin)
    sleep(6)

weatherDataMeasure()
pyautogui.keyDown('a')
sleep(3.1)
pyautogui.keyUp('a')

def asteroids():
    sleep(0.2)
    pyautogui.press('space')
    while pyautogui.locateOnScreen('reference-pictures/Asteroids.png') is None:
        pyautogui.click(clicks=20, interval=0.25)
        
asteroids()
