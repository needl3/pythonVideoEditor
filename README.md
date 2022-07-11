# Script to scrape and edit videos

This python script will help you download videos from different sources and do basic editing in then.
Below is the comprehensive usage manual

## Basic Functionalities

`----------------------------Menu----------------------------
1: Add Video                                 2: Add Audio
3: Clip                                      4: Concatenate video
5: Apply Filter                              6: Render
7: Clear Data                                8: Show Status
9: Exit                                      
------------------------------------------------------------`

### Adding videos
`
-----------------------Import Videos------------------------
1: Import from disk                          2: Import from YouTube
3: Import from TikTok                        4: Create from Text
5: Back
------------------------------------------------------------`
You can add and download videos simultaneously into your current project.
Downloading only supports:
	- YouTube
	- TikTok
- Option 1: You can also import locally saved videos.
- Option 2: Download and import video from YouTube video urls directly.
- Option 3: Download and import video from TikTok
	- Download from provided url
	- Download provided number of trending clips in your area
- Option 4: Create a clip from to be provided text. Will take a text input and generate a provided timed clip with that text. Easy to add some notes.

### Adding audios
Import locally saved audio into your project to be used in clips

### Importing videos as clips to edit
Clip imported videos or mark imported videos to be able to edit then
You can clip certain portion of the imported video by giving timestamp input as HR:MIN:SEC
For eg. 0:10:3 to select 10 minute 3 second timemark

### Apply Filters/Edit Videos
`-----------------------Select Filters-----------------------
1: fadein                                    2: fadeout
3: crop                                      4: changeSpeed
5: reverseClip                               6: rotateClip
7: resizeClip                                8: addText
9: paintClip                                 10: overlayAudio
11: removeAudio                               12: Back
------------------------------------------------------------`
Edit clips and apply different effects
Supported filters/edits:
	- `FadeIn` at the beginning of clip
	- `FadeOut` at the end of clip
	- `Crop` portion of clip
	- `ChangeSpeed` of clip
	- `Reverse` the clip flow
	- `Rotate` the clip orientation
	- `Resize` the clip dimensions
	- `AddText` over the clip providing the text position using coordinates
	- `Paint` the clip for ink painting effect
	- `OverlayAudio` to add audio onto the clip
	- `RemoveAudio` from the clip(Removes entire audio including the one being overlayed. So, advised to first remove audio then apply other overlaying audio)

`Note while using Filters:
Donot crop after applying filters. If you have to crop the clip. First crop and then apply needed filters`

### Concatenate clips
Sequence clips to be rendered. The position of clip in the concatenation sequence will determine the clip's queue.
You can check the concatenation sequence from main menu using option `8: Show Status` which will be displayed as:
Example: `-> [Clip 3] -> [Clip 1] -> [Clip 5] ->`

### Show project status
`-----------------------------Added Videos-----------------------------
	0: Name: helo
		Path: /home/needle/projects/moviepy/rendered/22_07_10_23_42_29.mp4
----------------------------------------------------------------------\
\
---------------------------Extracted Clips----------------------------
	0: Origin: helo
		Portion: [0, 51.57]
		Filters: ['addText']
----------------------------------------------------------------------\
\
------------------------Concatenation Sequence------------------------
	-> [Clip 0] -> [Clip 0] 
 ----------------------------------------------------------------------`
### Undo/Revert project variables
`-------------------------Clear data-------------------------
1: Video List                                2: Clip List
3: Concatenation List                        4: Audio List
5: All Data                                  6: Back
------------------------------------------------------------`
Reset project variables like:
- Imported videos
- Clips
- Clip from concatenation sequence
- Imported audio
- Everyting

### Render
`Moviepy - Building video /home/needle/projects/moviepy/rendered/22_07_11_20_03_56.mp4.
MoviePy - Writing audio in 22_07_11_20_03_56TEMP_MPY_wvf_snd.mp3
chunk:  61%|██████████████████████████████████████████████████████████████████▋                                           | 1379/2275 [00:00<00:00, 1449.76it/s, now=None]`

Renderes clips after concatenation according to the concatenation sequence