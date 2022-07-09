from utils.Crop import crop
import os
from moviepy.editor import vfx

def void():
	pass

def applyFilter(context):
	c = context.get("clips")
	for i,j in c.items():
		print(f"{i}: Clip ",j.get("portion"), " of ", context.get("videos").get(j.get("_id")).get("name"))

	# First select a clip to apply filters
	_id = int(input("Select clip to apply filter to:\n=>"))
	while _id not in c.keys():
		_id = int(input("Invalid id. Select again:\n=>"))

	# Now select a filter to apply
	return chooseFilter(c.get(_id).get("clip"))

def chooseFilter(clip):
	f = ["fadein", "fadeout", "crop", "changeSpeed", "reverseClip", "rotateClip", "resizeClip", "addText", "Back"]
	
	_ = None
	while _ != len(f):
		os.system("clear")

		# Select a filter
		print("Available filters".center(40, "-"))
		i=0
		for i in range(len(f)):
			if(i%2):
				print(f"{i+1}: {f[i]}")
			else:
				print(f"{i+1}: {f[i]}".ljust(20, " "), end="")
		_ = int(input("\nEnter an option: \n=>"))
		while(not _ or _ < 1 or _ > len(f)):
			_ = int(input("Invalid option. Enter again\n=>"))

		match _:
			case 1:
				applyFade(clip)
			case 2:
				applyFade(clip, out=True)
			case 3:
				applyCrop(clip)
			case 4:
				changeSpeed(clip)
			case 5:
				reverseClip(clip)
			case 6:
				rotateClip(clip)
			case 7:
				resizeClip(clip)
			case 8:
				return 0

def applyCrop(clip):
	x1, y1, x2, y2 = crop(clip.get_frame(10))
	clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
	return 0


def applyFade(clip, out=False):
	_ = input("Enter fade length(seconds)\n=>")
	while type(_) != int:
		_ = input("Invalid input: Enter again\n=>")

	if out:
		clip.fx(fadeout, _)
	else:
		clip.fx(fadein, _)

	return 0

def changeSpeed(clip):
	_ = None
	while(not _ or type(_) != float):
		try:
			_ = float(input("Enter a factor by which to change speed\n=>"))
		except ValueError:
			print("Invalid input")
	clip = clip.speedx(factor=_)
	return 0

def reverseClip(clip):
	clip = vfx.time_mirror(clip)
	return 0

def rotateClip(clip):
	_ = None
	while(not _ or type(_) != float):
		try:
			_ = float(input("Enter angle of rotation\n=>"))
		except ValueError:
			print("invalid input")
	clip = clip.add_mask().rotate(_)
	return 0

def resizeClip(clip):

	def parseResizeInput(inp):
		if "," in inp:
			_ = inp.split(",")
			if(len(_) == 2):
				width, height = _
				if width and not height:
					return ("w", width)
				elif height and not width:
					return ("h", height)
				elif width and height:
					return ("b", (width, height))
				else:
					print("No action defined")
			else:
				return None
		else:
			try:
				return float(inp)
			except ValueError:
				return None


	_ = None
	while _ == None:
		_ = parseResizeInput(input("Enter new size as:\
									\n1. width, height => Changes both\
									\n2. ,height => Changes height and adjusts width automatically\
									\n3. 0.0 - 1.0 => Computes new size based on original size and resize factor\
									\n=>"))
		if _ == None:
			print("Invalid input")
			return None
		elif type(_) == float:
			clip = clip.resize(_)
		elif len(_) == 2:
			match _[0]:
				case "w":
					clip = clip.resize(width=_[1])
				case "h":
					clip = clip.resize(height=_[1])
				case "b":
					clip = clip.resize(_[1])
				case _:
					print("Invalid input")
					_ = None

	clip.write_videofile("out.mp4")

	return 0

def addText(clip):
	# Set color from list
	# Set message(simple one line)
	# Set position
	# Preview
	# Done

	pass