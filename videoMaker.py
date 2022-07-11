import argparse
import cv2
import numpy as np
import os
from PIL import Image, FontFile, ImageFont, ImageDraw

class RenderText2Image:
	
	##Defines
	FULL_PATH_TO_FONT = 'assets/Edu_QLD_Beginner/EduQLDBeginner-VariableFont_wght.ttf'
	_bgcolor = None
	_fontColor = None
	_text = None
	_error, _errmsg = 1, None
	_outputFileName = None
	_img = None
	_font = None
	_draw = None
	_imgSize = (1200,800)
	_fontSize = 1

	def __init__(self, text=None, bgColor='#000000', fontColor='#FFFFFF', outputFileName="this.png", fontSize=0.5):
		##Set global vars
		self._text, self._bgcolor, self._fontColor = text, bgColor, fontColor
		self._outputFileName = outputFileName
		self._fontSize = fontSize
		self.makeBackground()
		

	def makeBackground(self):
		try:
			self._img = Image.new("RGB", self._imgSize, self._bgcolor)
			self._draw = ImageDraw.Draw(self._img)
			if not self._text:
				self._img.save(self._outputFileName, "PNG")
				print("Blank frame created as ",self._outputFileName)
				return
			self.setFontSize()
		except Exception:
			self._error, self._errmsg = 0, "Background could not be rendered ERR_MSG:"
	
	def setFontSize(self):
		fontsize = 1
		img_fraction = float(self._fontSize)
		try:
			self._font = ImageFont.truetype(self.FULL_PATH_TO_FONT, fontsize)
			while self._font.getsize(self._text)[0] < img_fraction * self._img.size[0]:
				fontsize += 1
				self._font = ImageFont.truetype(self.FULL_PATH_TO_FONT, fontsize)
		except Exception as e:
			print("ERROR WITH FONT", e)
			
		self.addText2Image()
	
	def parseText(self):
		import textwrap
		lines = textwrap.wrap(self._text, 60)
		return lines
	
	def addText2Image(self):
		lines = self.parseText()
		try:
			count = 0
			self._draw.text((self._imgSize[0]*0.1,self._imgSize[1]*0.4), self._text, fill=self._fontColor, font=self._font, align="center")
			self._img.save(self._outputFileName, "PNG")
			print("Image saved as: ", self._outputFileName)
		except Exception:
			print("Exception while adding text ot image")
			
	def getImage(self):
		return self._outputFileName if self._error else self._error

class ImageToVideo:
	_outDir = os.path.abspath("./downloaded_vids/")
	def __init__(self, output):
		self.output = self._outDir+"/"+output+".avi"

		if not os.path.exists(self._outDir):
			os.makedirs(self._outDir)

	def generate_frames(self, filename, sec, exception=False):
		if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or exception:
			img = cv2.imread(filename)
			height, width, layers = img.shape
			size = (width,height)
		else:
			print("[Task failed]***Input valid image***")
			return
		fps=20
		print("Framerate set as ", fps," frame/sec.")

		out = cv2.VideoWriter(self.output,0, fps, size)
		
		print("Creating video stream")
		for i in range(int(sec*fps)):
			out.write(img)
		out.release()
		os.remove(filename)
		print("Video released as ", self.output)
		return self.output

def textToClip(text, output, bgColor='#000000', fontColor='#FFFFFF', sec=5, fontSize=1):
	print("Received: ", text, output, bgColor, fontColor, sec, fontSize)
	frame = RenderText2Image(text=text, bgColor=bgColor, fontColor=fontColor, fontSize=fontSize).getImage()
	return ImageToVideo(output).generate_frames(frame, sec)