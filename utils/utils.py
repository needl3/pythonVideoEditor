def parseDuration(durationStr):
	try:
		hr, mn, sec = durationStr.split(":")
		return int(hr) * 60 * 60+int(mn) * 60+int(sec)
	except ValueError:
		return 0