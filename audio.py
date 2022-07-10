from utils.context import context
from utils.utils import displayOptions, chooseFile

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
		_ = displayOptions(op, "Import Audio")
		match _:
			case 1:
				importFromDisk()
			case 2:
				return 0
			case _:
				print("Invalid input")