import datetime
from .utils import displayOptions

DOWNLOAD_DIR = "downloaded_vids"

def downloadFromTiktok(name):
	from TikTokAPI import TikTokAPI

	api = TikTokAPI()

	def downloadTrending(count=5):
		r = api.getTrending(count=count)
	
		# Slicing because api doesn't return specified count
		for i in r.get("items")[:count]:
			v_id = i.get("id")
			print(f"Downloading {v_id}: {i.get('desc')}")
			api.downloadVideoById(v_id, f"{DOWNLOAD_DIR}/{name}-{datetime.datetime.today().strftime('%y_%m_%d_%H_%M_%S')}.mp4")

	def downloadFromUrl(url):
		def parseId(url):
			u = None
			try:
				u = url.split("video/")[1].split("?")[0]
			except:
				u = input("Invalid url. Input id yourself.")
			return u

		try:
			out_file = f"{DOWNLOAD_DIR}/{name}.mp4"
			print(f"Downloading as {out_file}")
			api.downloadVideoById(parseId(url), out_file)
			return out_file
		except:
			print("Cannot download video. Maybe network is down or the id is invalid")
			return 1

	op = ["Download Bulk Trending", "Download from Url", "Back"]

	_ = displayOptions(op, "TikTok Downloader")

	match _:
		case 1:
			inp_count = None
			while not inp_count:
				try:
					inp_count = int(input("Enter no of video to download\n=>"))
				except:
					print("Invalid input")
			return downloadTrending(count = inp_count)
		case 2:
			return downloadFromUrl(input("Enter video url:\n=>"))


def downloadFromYT(name):
	name += ".mp4"
	url = input("Enter youtube url:\n=>")

	from pytube import YouTube
	try:
		print("Downloading... Please wait...")
		yt = YouTube(url)
	except:
		print("[X] Connection Error")
		return 1

	try: 
		yt.streams.filter(file_extension="mp4").first().download(DOWNLOAD_DIR, name)
		return os.path.abspath(f"{DOWNLOAD_DIR}/{name}")
	except Exception as e: 
		print("[X] Download Error!", e) 
		return None

def downloadFromFacebook(name):
	pass
def downloadFromInstagram(name):
	pass