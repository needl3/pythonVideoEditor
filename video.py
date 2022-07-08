import os
import  tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from utils.utils import parseDuration

def chooseVideo():
	import  tkinter as tk
	from tkinter import filedialog
	root = tk.Tk()
	root.withdraw()
	return filedialog.askopenfilename()

def downloadFromYT(name):
	url = input("Enter youtube url:\n=>")
	from pytube import YouTube
	try:
		print("Downloading... Please wait...")
		yt = YouTube(url)
	except:
		print("[X] Connection Error")
		return 1

	try: 
		yt.streams.filter(file_extension="mp4").first().download("downloaded_vids", name)
		return os.path.abspath(f"downloaded_vids/{name}")
	except: 
		print("[X] Download Error!") 
		return None

def downloadFromFacebook():
	pass
def downloadFromInstagram():
	pass

def addVideo(context):
	os.system("clear")

	o = ["Import from disk", "Import from YouTube", "Back"]
	i=0
	while i < len(o):
		print(str(i+1) + ": " + o[i].ljust(20, " "), end="")
		if i < len(o)-1:
			i += 1
		else:
			break
		print(str(i+1) + ": "+o[i])
		i+=1
	op = int(input("\nEnter an option: \n=>"))
	while(not op or op < 1 or op > len(o)):
		op = int(input("Invalid option. Enter again\n=>"))

	path = str()
	import_name = input("Enter name for the import:\n=>")
	_id = len(context.get("videos"))
	match op:
		case 1:
			path = chooseVideo()
		case 2:
			path = downloadFromYT(import_name)
		case 3:
			return

	if path:
		context["videos"][id] = {
			"name": import_name,
			"path": path
		}
	else:
		print("[X] Cannot add video")

def clipVideo(context):
	vids = context.get("videos")
	print("Added videos".center(40, "-"))
	for i,j in vids.items():
		print(f"{i}: {vids.get(i).get('name')}")
	
	_id = int(input("Select video to clip:\n=>"))
	while _id not in vids.keys():
		_id = int(input("Invalid id. Select again:\n=>"))

	selected = VideoFileClip(vids.get(_id).get("path"))

	print(f"Video {vids.get(_id).get('name')} selected. [ Duration: {selected.duration}]")
	
	print("If no duration is entered, whole video will be considered as a clip")
	start = parseDuration(input("Input the start of clip in HR:MIN:SEC\n=>"))
	end = parseDuration(input("Input the end of clip in HR:MIN:SEC\n=>"))
	if not end:
		end = selected.duration

	context["clips"][len(context.get("clips"))] = {
		"_id": _id,
		"portion": [start, end],
		"clip": selected.subclip(start, end)
	}
	return 0

def concatenateVideo(context):
	c = context.get("clips")
	for i,j in c.items():
		print(f"{i}: Clip ",j.get("portion"), " of ", context.get("videos").get(j.get("_id")).get("name"))

	while True:
		_id = int(input("Select clip in sequence to concatenate:\n=>"))
		while _id not in c.keys():
			_id = int(input("Invalid id. Select again:\n=>"))
		context["concat"].append(_id)
		if input("Add more?(y/n)").lower() == "n":
			break




