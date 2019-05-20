# buat 2 inputbox  di html masukan 2 input
# contoh input -> x = 1,2,3,4,5,6 y = 4,5,6,8,7
# output plot dari matplotlib

from flask import Flask, render_template
from  import my_plotter
import requests

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# hasil_gambar
@app.route('/results', methods=['POST'])
def results():
    x = requests.form
    y = requests.form


if __name__ == '__main__':
    app.run(debug=True)

