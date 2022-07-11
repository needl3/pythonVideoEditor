#!venv/bin/python

import os
from video import addVideo, concatenateVideo, clipVideo
from audio import addAudio
from render import render
from filter import applyFilter, resizeClip
from utils.utils import clearData, displayOptions, addTest, showStatus

from moviepy.editor import VideoFileClip

from utils.context import context, CLEAR

def dot(width, msg):
    if(width < len(msg)):
        print("Invalid width")
        return

    for i in range((width-len(msg))//2):
        print("-", end="")

    print(msg, end="")

    for i in range((width-len(msg))//2):
        print("-", end="")
    print("\n")

def menu():
    op = ["Add Video", "Add Audio", "Clip", "Concatenate video", "Apply Filter", "Render", "Clear Data", "Show Status", "Exit"]

    # addTest()

    _ = None
    while _ != len(op):
        os.system(CLEAR)
        _ = displayOptions(op, "Menu")

        match _:
            case 1:
                addVideo()
            case 2:
                addAudio()
            case 3:
                clipVideo()
            case 4:
                concatenateVideo()
            case 5:
                applyFilter()
            case 6:
                render()
            case 7:
                clearData()
            case 8:
                showStatus()
            case 9:
                print("Thank you for using!")
            case 10:
                print(context)
            case _:
                print("Invalid input")

if __name__ == "__main__":
    menu()