from moviepy.editor import concatenate_videoclips
import os
import datetime
from utils.context import context

OUT_DIR = os.path.abspath(".")+"/rendered/"

def render():
	# Prepare out directory
	if not os.path.exists(OUT_DIR):
		os.makedirs(OUT_DIR)

	clips = [context.get("clips").get(i).get("clip") for i in context.get("concat")]

	if not bool(clips):
		print("No concatenated files to render. Maybe you forgot to add in concatenation queue?")
		return 1

	final = concatenate_videoclips(clips)
	final_filename = OUT_DIR+\
		datetime.datetime.today().strftime("%y_%m_%d_%H_%M_%S")+\
		".mp4"
	final.write_videofile(final_filename)
	return 0
