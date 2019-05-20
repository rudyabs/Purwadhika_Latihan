# buat 2 inputbox  di html masukan 2 input
# contoh input -> x = 1,2,3,4,5,6 y = 4,5,6,8,7
# output plot dari matplotlib

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from _function import my_plotter
import matplotlib.pyplot as plt
import requests



app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# hasil_gambar
@app.route('/results', methods=['POST'])
def results():
    x = request.form['data1']
    y = request.form['data2']
    data1 = []
    data2 = []
    for i in x.split(','):
        data1.append(int(i))
    for i in y.split(','):
        data2.append(int(i))
    
    plt.close()
    plt.figure('Figure X dan Y', figsize=(10,5))
    plt.plot(data1, data2, marker='o')
    plt.title('Plot Results')
    plt.grid(True)
    plt.xlabel('X')
    plt.xticks(data1)
    plt.ylabel('Y')
    plt.yticks(data2)
    plt.savefig('gambar/results.png')


    file_name = 'results.png'

    return redirect(url_for('image', x = file_name))

@app.route('/gambar/<path:x>')
def image(x):
    return send_from_directory('gambar', x)
    

if __name__ == '__main__':
    app.run(debug=True)

