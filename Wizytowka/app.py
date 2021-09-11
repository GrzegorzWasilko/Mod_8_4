from app import message
from flask import Flask , render_template ,url_for
from flask import request, redirect

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('me.html')


@app.route('/contact', methods = ['GET', 'POST'] )
def contact():

    if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")

    elif request.method == 'POST':
       print("\nWe received POST\n")
       message=request.form['message']
       print(f"otrzymana wiadomosc to: {message}")
    return render_template("me.html")
