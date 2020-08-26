import os
import json
from pprint import pprint
from flask import Flask, request
from flask_cors import CORS

DUMP_DIR = "archive"
app = Flask(__name__)
CORS(app)

@app.route("/save", methods=["POST"])
def update():
	last = int(max(os.listdir(DUMP_DIR), default="0").split(".")[0], 16)
	tag = ""
	ext = request.json["url"].split(".")[-1]
	if ext != "" and len(ext) <= 16 and "/" not in ext: tag += "." + ext
	fn = "%s/%08x%s.json" % (DUMP_DIR, last + 1, tag)
	with open(fn, "xt") as f:
		json.dump(request.json, f)
	print(request.json["url"])
	return "", 204

if __name__ == "__main__":
	os.makedirs(DUMP_DIR, exist_ok=True)
	import logging
	logging.basicConfig(level=logging.INFO)
	app.run()
else:
	# Worker startup. This is the place to put any actual initialization work
	# as it won't be done on master startup.
	...
