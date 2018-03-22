#!/usr/bin/python3
import pyautogui
import time

# use this to find the x and y coordinate of the text box to enter text
print (pyautogui.position())

# x and y coordinate of textbox
textBoxX = 564
textBoxY = 1057

spam = input ('Enter spam message here: ')

limit = 0
while (limit < 10): 
    pyautogui.click(textBoxX, textBoxY) # click text box
    pyautogui.typewrite(spam) # write spam
    pyautogui.press('enter') # press carriage return (send spam)
    limit = limit + 1
    time.sleep(.200) # wait 0.2 seconds