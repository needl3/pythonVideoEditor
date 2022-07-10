import os
from utils.context import context
import  tkinter as tk
from tkinter import filedialog

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
	os.system("clear")
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
				print(f"{i}: {j.get('name')}")
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

		os.system("clear")

def displayOptions(op, title):
	print(title.center(40, "-"))
	i=0
	while i < len(op):
		print(str(i+1) + ": " + op[i].ljust(20, " "), end="")
		if i < len(op)-1:
			i += 1
		else:
			break
		print(str(i+1) + ": "+op[i])
		i+=1

	_ = None
	print("".center(40, "-")+"\n")
	while(not _ or _ < 1 or _ > len(op)+1):
		try:
			_ = int(input("Enter valid option\n=>"))
		except ValueError:
			print("Invalid option chosen")
	
	return _