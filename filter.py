from utils.Crop import crop
import os
from moviepy.editor import vfx, AudioFileClip, TextClip, CompositeVideoClip

from utils.context import context, CLEAR
from utils.utils import displayOptions

def void():
	pass

def applyFilter():

	c = context.get("clips")
	if not bool(c):
		print("No clips added to apply filter to")
		print("Press Enter to go back")
		input()
		return 1

	for i,j in c.items():
		print(f"{i}: Clip ",j.get("portion"), " of ", context.get("videos").get(j.get("_id")).get("name"))

	# First select a clip to apply filters
	_id = None
	while _id not in c.keys():
		try:
			_id = int(input("Select valid clip id:\n=>"))
		except:
			print("Invalid id chosen")


	# Now select a filter to apply
	try:
		context["clips"][_id]["filters"]
	except KeyError:
		context["clips"][_id]["filters"] = []
	return chooseFilter(_id)

def chooseFilter(_id):
	f = ["fadein", "fadeout", "crop", "changeSpeed",\
	"reverseClip", "rotateClip", "resizeClip", "addText",\
	"paintClip", "overlayAudio", "removeAudio", "Back"]
	
	_op = None
	while True:
		os.system(CLEAR)

		# Select a filter
		# This problem is because applying filters corrupts raw data
		# Maybe because it does internal compressions
		print("Note: Do not crop after applying any of the filter.\nIf you need to crop, then crop first and apply other filters")
		_op = displayOptions(f, "Select Filters")

		match _op:
			case 1:
				applyFade(_id)
			case 2:
				applyFade(_id, out=True)
			case 3:
				applyCrop(_id)
			case 4:
				changeSpeed(_id)
			case 5:
				reverseClip(_id)
			case 6:
				rotateClip(_id)
			case 7:
				resizeClip(_id)
			case 8:
				addText(_id)
			case 9:
				paintClip(_id)
			case 10:
				overlayAudio(_id)
			case 11:
				removeAudio(_id)
			case 12:
				return 0
			case _:
				print("Invalid Input.")

	return None
def overlayAudio(_id):
	clip = context.get("clips").get(_id).get("clip")

	print("Overlay Audio".center(40, "-"))
	print("Note: You can even choose video for automatic extraction")
	for i,j in context.get("audio").items():
		print(f"{i+1}: {j.get('name')}")

	_op = None
	while _op not in context.get("audio").keys():
		try:
			_op = int(input("Select Audio to apply\n=>"))-1
		except ValueError:
			print("Invalid input")
	audio = AudioFileClip(context.get("audio").get(_op).get("path")).subclip(0, clip.duration)
	context["clips"][_id]["clip"] = clip.set_audio(audio)

	context["clips"][_id]["filters"].append(overlayAudio.__name__)

	return 0

def applyCrop(_id):
	clip = context.get("clips").get(_id).get("clip")

	#
	# TODO: Make a function to get a random frame within limits
	#
	try:
		x1, y1, x2, y2 = crop(clip.get_frame(10))
	except:
		print("Cannot crop the clip. Make sure no filters were applied on it till now.")
		input("Press enter to return...")
		return 1
	clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2).resize(width=abs(x1-x2))
	
	context["clips"][_id]["clip"] = clip

	context["clips"][_id]["filters"].append(applyCrop.__name__)

	return 0


def applyFade(_id, out=False):
	clip = context.get("clips").get(_id).get("clip")
	try:
		_op = float(input("Enter fade length(seconds)\n=>"))
	except ValueError:
		pass
	while type(_op) != float:
		try:
			_op = float(input("Invalid input: Enter again\n=>"))
		except ValueError:
			pass


	if out:
		clip = clip.fx(vfx.fadeout, _op)
		context["clips"][_id]["filters"].append("fadeOut")
	else:
		clip = clip.fx(vfx.fadein, _op)
		context["clips"][_id]["filters"].append("fadeIn")

	context["clips"][_id]["clip"] = clip

	return 0

def changeSpeed(_id):
	clip = context.get("clips").get(_id).get("clip")

	_op = None
	while(not _op or type(_op) != float):
		try:
			_op = float(input("Enter a factor by which to change speed\n=>"))
		except ValueError:
			print("Invalid input")
	clip = clip.speedx(factor=_op)

	context["clips"][_id]["clip"] = clip

	context["clips"][_id]["filters"].append(changeSpeed.__name__)

	return 0

def reverseClip(_id):
	clip = context.get("clips").get(_id).get("clip")

	clip = vfx.time_mirror(clip)

	context["clips"][_id]["clip"] = clip

	context["clips"][_id]["filters"].append(reverseClip.__name__)
	return 0

def rotateClip(_id):
	clip = context.get("clips").get(_id).get("clip")

	_op = None
	while(not _op or type(_op) != float):
		try:
			_op = float(input("Enter angle of rotation\n=>"))
		except ValueError:
			print("invalid input")
	try:
		clip = clip.add_mask().rotate(_op)
	except:
		print("Rotation failed. Make sure to not apply any other filters before applying this.")
		input("Press enter to return")
		return 1

	context["clips"][_id]["clip"] = clip

	context["clips"][_id]["filters"].append(rotateClip.__name__)
	return 0

def resizeClip(_id):
	clip = context.get("clips").get(_id).get("clip")

	def parseResizeInput(inp):
		if "," in inp:
			_op = inp.split(",")
			if(len(_op) == 2):
				width, height = _op
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


	_op = None
	while _op == None:
		_op = parseResizeInput(input("Enter new size as:\
									\n1. width, height => Changes both\
									\n2. ,height => Changes height and adjusts width automatically\
									\n3. 0.0 - 1.0 => Computes new size based on original size and resize factor\
									\n=>"))
		if _op == None:
			print("Invalid input")
			return None
		elif type(_op) == float:
			clip = clip.resize(_op)
		elif len(_op) == 2:
			match _op[0]:
				case "w":
					clip = clip.resize(width=_op[1])
				case "h":
					clip = clip.resize(height=_op[1])
				case "b":
					clip = clip.resize(_op[1])
				case _:
					print("Invalid input")
					_op = None


	context["clips"][_id]["clip"] = clip

	context["clips"][_id]["filters"].append(resizeClip.__name__)

	return 0

def paintClip(_id):
	clip = context.get("clips").get(_id).get("clip")

	_op = None
	while not _op or type(_op) != float:
		try:
			_op = input("Enter paint saturation strength(default: 1.4):\n=>")
			if not bool(_op):
				_op = 1.4
				break
			else:
				raise ValueError
		except ValueError:
			print("Invalid input")
	clip = clip.fx(vfx.painting, _op)

	context["clips"][_id]["clip"] = clip

	context["clips"][_id]["filters"].append(paintClip.__name__)

	return 0

def removeAudio(_id):
	clip = context.get("clips").get(_id).get("clip")

	context["clips"][_id]["clip"] =  clip.without_audio()

	context["clips"][_id]["filters"].append(applyFade.__name__)

	return 0

def addText(_id):
	clip = context.get("clips").get(_id).get("clip")

	# Set color from list
	# Set message(simple one line)
	size = None
	while not size:
		try:
			size = float(input("Enter font size\n=>"))
		except:
			print("Invalid input")

	print("Available Primary Colors:")
	colors = ["black", "white", "blue", "green", "orange", "red", "purple"]
	for i in colors:
		print(i, end=", ")
	print("\n")
	c = None
	while c not in [i.decode() for i in TextClip.list("color")]:
		c = input("Enter valid text color:\n=>")

	t = TextClip(input("Enter text to add:\n=>"), fontsize=size, color=c)
	# Set position
	pos = None
	dur = None
	while not pos:
		try:
			pos = input("Enter text position in (x,y) or from the list: [center, bottom, top]\n=>")
			if pos not in ["center", "bottom", "top"]:
				raise TypeError
		except:
			print("Invalid input")

	while not dur:
		try:
			dur = float(input("Enter clip duration\n=>"))
		except:
			print("Invalid Input")

	t = t.set_pos(pos).set_duration(dur)

	# Done
	context["clips"][_id]["clip"] = CompositeVideoClip([clip, t])
	context["clips"][_id]["filters"].append(addText.__name__)

	return 0