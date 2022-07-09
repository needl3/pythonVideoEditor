#!venv/bin/python

import os
from video import addVideo, concatenateVideo, clipVideo
from audio import addAudio
from render import render
from filter import applyFilter, resizeClip

from moviepy.editor import VideoFileClip

context ={
    "videos":dict(),
    "audio":dict(),
    "filters":dict(),
    "clips":dict(),
    "concat":list()
}

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
    op = ["Add Video", "Add Audio", "Clip", "Concatenate video", "Apply Filter", "Render", "Exit"]
    _ = None
    while _ != len(op):
        os.system("clear")
        print("Menu".center(40, "-"))
        i=0
        while i < len(op):
            print(str(i+1) + ": " + op[i].ljust(20, " "), end="")
            if i < len(op)-1:
                i += 1
            else:
                break
            print(str(i+1) + ": "+op[i])
            i+=1

        _ = int(input("\nEnter an option: \n=>"))
        while(not _ or _ < 1 or _ > len(op)+1):
            _ = int(input("Invalid option. Enter again\n=>"))

        context["videos"][0] = {
            "name": "hemlo",
            "path": os.path.abspath("/home/needle/Downloads/example.mp4")
        }
        context["videos"][1] = {
            "name": "hemlo",
            "path": os.path.abspath("/home/needle/Downloads/example.mp4")
        }
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
        match _:
            case 1:
                addVideo(context)
            case 2:
                addAudio(context)
            case 3:
                clipVideo(context)
            case 4:
                concatenateVideo(context)
            case 5:
                applyFilter(context)
            case 6:
                render(context)
            case 7:
                print("Thank you for using!")
            case 8:
                print(context)

if __name__ == "__main__":
    menu()