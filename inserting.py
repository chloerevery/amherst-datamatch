from flask import Flask, request, session, g, redirect, url_for, abort, render_template

from pymongo import MongoClient
client=MongoClient('localhost', 27017)
db=client.amherst_datamatch
participants=db.participants

# creates the application
app = Flask(__name__)
#app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def starting_page():
    return render_template('index.html')

@app.route('/completed', methods = ['POST'])
def insert_participant():
    participant = {
        "name": request.form['name'],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "class": request.form['class'],
        "gender":request.form['gender'],
        "seeking":request.form['seeking'],
        "one": request.form["one"],
        "two": request.form["two"],
        "three": request.form["three"],
        "four": request.form["four"],
        "five": request.form["five"],
        "six": request.form["six"],
        "seven": request.form["seven"],
        "eight": request.form["eight"],
        "nine": request.form["nine"],
        "ten": request.form["ten"]       
        }
    participants.insert(participant)
    return render_template('completed.html')

if __name__ == '__main__':
    app.debug=True          #restarts every time you change code
    app.run()
    
    
    
