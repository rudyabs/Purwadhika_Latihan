# pada saat selesai upload buat page baru dengan file yang sudah terupload
from flask import Flask, render_template
app = Flask(__name__)

# HOME route
@app.route("/")
def home():
    return render_template("033lat-homepage.html")

# 404 error handle
@app.errorhandler(404)
def error_404(error):
    return render_template("033lat-404.html")

# upload route
@app.route("/upload")
def upload():
    return render_template()

if __name__ == "__main__":
    app.run(debug = True)

