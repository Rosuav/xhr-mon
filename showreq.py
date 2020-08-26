import json
import base64
import sys
if len(sys.argv) < 2:
	sys.exit(0, "USAGE: python3 showreq.py archive/SOME_FILE.json")

for fn in sys.argv[1:]:
	try: f = open(fn)
	except FileNotFoundError: f = open("archive/" + fn)
	with f: req = json.load(f)
	print(req["url"], file=sys.stderr)
	if req["type"] == "arraybuffer":
		data = req["data"]
		if isinstance(data, str):
			# Early files had a multi-level encoding b/c I didn't know btoa wouldn't do what I wanted
			data = base64.b64decode(data).decode()
			data = [int(x) for x in data.split(",")]
		# Otherwise it should already be a list of integers.
		data = bytes(data)
		try: data = data.decode("utf-8")
		except UnicodeDecodeError: data = repr(data)
		print(data)
