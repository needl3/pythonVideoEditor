import os
from moviepy.editor import VideoFileClip
from utils.utils import parseDuration, displayOptions, chooseFile

from utils.context import context



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

def addVideo():
	while True:
		os.system("clear")

		o = ["Import from disk", "Import from YouTube", "Back"]

		_ = displayOptions(o, "Import Videos")

		path = str()
		match _:
			case 1:
				path = chooseFile()
			case 2:
				path = downloadFromYT()
			case 3:
				return

		_id = len(context.get("videos"))
		if bool(path):
			context["videos"][_id] = {
				"name": input("Enter name for the import:\n=>"),
				"path": path
			}
		else:
			print("[X] Cannot add video")

def clipVideo():
	vids = context.get("videos")
	if not bool(vids):
		print("No clips added to apply filter to.")
		input("Press Enter to go back")
		input()
		return

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

def concatenateVideo():
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