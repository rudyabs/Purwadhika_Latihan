from flask import Flask, request, render_template, jsonify, flash, redirect, url_for, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import Articles



app = Flask(__name__)
Articles = Articles()


# configure mysql
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "rudyabs"
app.config["MYSQL_PASSWORD"] = "Kecapi48"
app.config["MYSQL_DB"] = "flask_app"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# menjalankan sql
MySQL = MySQL(app)


# home route
@app.route("/")
def home():
    return render_template("home.html")

# about route
@app.route("/about")
def about():
    return render_template("about.html")

# articles route
@app.route("/articles")
def articles():    
    return render_template("articles.html", articles = Articles)

# article route
@app.route("/article/<string:id>")
def article(id):    
    return render_template("article.html", id = id)

# wtform
class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=1, max=100)])
    username = StringField('Username', [validators.length(min=4, max=30)])
    email = StringField('Email', [validators.length(min=6, max=100)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.equal_to('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

# signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    # cek apakah post atau get
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #   membuat cursor sql
        cur = MySQL.connection.cursor()

        # menjalankan query
        cur.execute("insert into users(name, email, username, password) values(%s, %s, %s, %s)", (name, email, username, password))

        #   commit to DB
        MySQL.connection.commit()

        # close connection
        cur.close()

        flash("Registrasi telah berhasil", "success")

        redirect(url_for('home'))
    return render_template('signup.html', form = form)    

if __name__ == "__main__":
    app.secret_key='rahasia123'
    app.run(debug= True)