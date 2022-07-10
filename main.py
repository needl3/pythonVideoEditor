#!venv/bin/python

import os
from video import addVideo, concatenateVideo, clipVideo
from audio import addAudio
from render import render
from filter import applyFilter, resizeClip
from utils.utils import clearData, displayOptions

from moviepy.editor import VideoFileClip

from utils.context import context

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
    op = ["Add Video", "Add Audio", "Clip", "Concatenate video", "Apply Filter", "Render", "Clear Data", "Exit"]

    # Adding videos for test
    context["videos"][0] = {
        "name": "hemlo",
        "path": os.path.abspath("/home/needle/Downloads/example.mp4")
    }
    context["videos"][1] = {
        "name": "hemlo",
        "path": os.path.abspath("/home/needle/Downloads/example.mp4")
    }

    # Adding clips for test
    selected = VideoFileClip(os.path.abspath("/home/needle/Downloads/example.mp4"))
    context["clips"][0] = {
        "_id": 0,
        "portion": [10, 20],
        "clip": selected.subclip(10, 20)
    }
    context["clips"][1] = {
        "_id": 1,
        "portion": [20, 30],
        "clip": selected.subclip(20, 30)
    }
    # Adding audio for test
    context["audio"][0] = {
        "name": "myaudio",
        "path": "/home/needle/Downloads/example.mp3"
    }
    _ = None
    while _ != len(op):
        os.system("clear")
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
                print("Thank you for using!")
            case 9:
                print(context)
            case _:
                print("Invalid input")

if __name__ == "__main__":
    menu()