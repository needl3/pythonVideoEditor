


def chooseFilter(clip):
	print("Need to implement this huge deal")

def applyFilter(context):
	c = context.get("clips")
	for i,j in c.items():
		print(f"{i}: Clip ",j.get("portion"), " of ", context.get("videos").get(j.get("_id")).get("name"))

	while True:
		# First select a clip to apply filters
		_id = int(input("Select clip to apply filter to:\n=>"))
		while _id not in c.keys():
			_id = int(input("Invalid id. Select again:\n=>"))

		# Now select a filter to apply
		chooseFilter(c.get(_id).get("clip"))

		if input("Add more?(y/n)").lower() == "n":
			break
