from flask import *
import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", result=os.listdir(os.path.join("static", "Audios")))

@app.route("/upload")
def upload():
	return render_template("upload.html")

@app.route("/b-upload", methods=["POST"])
def b_upload():
	if request.method == "POST":
		name = request.form["name"]
		audio = request.files["audio"]

		audio.save(os.path.join("static", "Audios", name+".mp3"))
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug=True, port=4444)