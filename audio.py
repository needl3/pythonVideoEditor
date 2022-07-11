from utils.context import context, CLEAR
from utils.utils import displayOptions, chooseFile
import os

def void():
	pass

def importFromDisk():
	file_path = chooseFile()
	if not bool(file_path):
		print("No file chosen")
		return 1
	
	_id = len(context["audio"])+1
	context["audio"][_id] = {
		"name": input("Name your import\n=>"),
		"path": file_path
	}
	return 0

def addAudio():
	op = ["From local disk", "Back"]
	

	while True:
		os.system(CLEAR)
		_op = displayOptions(op, "Import Audio")
		match _op:
			case 1:
				importFromDisk()
			case 2:
				return 0
			case _op:
				print("Invalid input")