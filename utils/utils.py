import os
from utils.context import context, CLEAR
import  tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def addTest():
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

def chooseFile():
	import  tkinter as tk
	from tkinter import filedialog
	root = tk.Tk()
	root.withdraw()
	return filedialog.askopenfilename()

def parseDuration(durationStr):
	try:
		hr, mn, sec = durationStr.split(":")
		return int(hr) * 60 * 60+int(mn) * 60+int(sec)
	except ValueError:
		return 0

def clearData(debug = False):
	os.system(CLEAR)
	def clearVideo():
		while True:
			print("Clear Video".center(40, "-"))
			for i,j in context.get("videos").items():
				print(f"{i}: {j.get('name')}")
			_ = None
			while not _ or _ not in context.get("videos").keys():
				try:
					_ = int(input("Enter video id to remove\n=>"))
				except:
					print("Invalid input")

			del context["videos"][_]

			if input("Remove another?(Y/N)\n=>").lower() != "y":
				break
	def clearClips():
		l_clips = context.get("clips")
		while bool(l_clips):
			print("Clear Clips".center(40, "-"))
			for i,j in l_clips.items():
				print(f"{i}: {context.get('videos').get(j.get('_id')).get('name')}")
			_ = None
			while _ not in l_clips.keys():
				try:
					_ = int(input("Enter clip id to remove\n=>"))
				except:
					print("Invalid input")
					return 1

			del context["clips"][_]
			if _ in context.get("concat"):
				del context["concat"][_]

			if input("Remove another?(Y/N)\n=>").lower() != "y":
				break
	def clearConcatenated():
		l_concat = context.get("concat")
		while bool(l_concat):
			print("Clear from Concatenation queue".center(40, "-"))
			for i in l_concat:
				print(f"{i}: {context.get('videos').get(context.get('clips').get(i).get('_id')).get('name')} from {context.get('clips').get(i).get('portion')}")
			_ = None
			while _ not in l_concat and _ != l_concat[-1]+1:
				try:
					_ = int(input("Enter clip id to remove\n=>"))
				except:
					print("Invalid input")
					return

			del context["concat"][l_concat.index(_)]

			if input("Remove another?(Y/N)\n=>").lower() != "y":
				break

	def clearAudio():
		l_audio = context.get("audio")
		while bool(l_audio):
			print("Clear Audio".center(40, "-"))
			for i,j in l_audio.items():
				print(f"{i}: {j.get('name')}")
			_ = None
			while _ not in l_audio.keys():
				try:
					_ = int(input("Enter clip id to remove\n=>"))
				except:
					print("Invalid input")
					return 1

			del context["audio"][_]
			
			if input("Remove another?(Y/N)\n=>").lower() != "y":
				break

	while True:
		op = ["Video List", "Clip List", "Concatenation List", "Audio List", "All Data", "Back"]

		_ = displayOptions(op, "Clear data")

		match _:
			case 1:
				clearVideo()
			case 2:
				clearClips()
			case 3:
				clearConcatenated()
			case 4:
				clearAudio()
			case 5:
				if input("Are you sure you want to reset all data?(Y/N):\n=>").lower() == "y":
					print("Clearing all data")
					for i,j in context.items():
						context[i].clear()
			case 6:
				return
			case _:
				print("Invalid option. Going back..")

		os.system(CLEAR)

def displayOptions(op, title):
	PADDING = 60
	print(title.center(PADDING, "-"))
	i=0
	while i < len(op):
		print(str(i+1) + ": " + op[i].ljust(int(PADDING*0.7), " "), end="")
		if i < len(op)-1:
			i += 1
		else:
			break
		print(str(i+1) + ": "+op[i])
		i+=1

	_ = None
	print("\n"+"".center(PADDING, "-")+"\n")
	while(not _ or _ < 1 or _ > len(op)+1):
		try:
			_ = int(input("Enter valid option\n=>"))
		except ValueError:
			print("Invalid option chosen")
	
	return _

def showStatus():
	PADDING = 70
	l_vids = context.get("videos")
	if bool(l_vids):
		print("Added Videos".center(PADDING, "-"))
		for i,j in l_vids.items():
			print(f"\t{i}: Name: {j.get('name')}\n\t\tPath: {j.get('path')}")
		print("-"*PADDING, "\n")

	l_clips = context.get("clips")
	if bool(l_clips):
		print("Extracted Clips".center(PADDING, "-"))
		for i,j in l_clips.items():
			print(f"\t{i}: Origin: {l_vids.get(j.get('_id')).get('name')}")
			print(f"\t\tPortion: {j.get('portion')}")
			print(f"\t\tFilters: {j.get('filters')}")
		print("-"*PADDING, "\n")

	l_audio = context.get("audio")
	if bool(l_audio):
		print("Added audio".center(PADDING, "-"))
		for i,j in l_audio.items():
			print(f"\t{i}: Name: {j.get('name')}\n\t\tPath: {j.get('path')}")
		print("-"*PADDING, "\n")

	l_concat = context.get("concat")
	if bool(l_concat):
		print("Concatenation Sequence".center(PADDING, "-"), end="\n\t")
		for i in l_concat:
			print(f"-> [Clip {i}] ", end="")
		print("\n", "-"*PADDING, "\n")

	input("Press Enter to go to main menu...")