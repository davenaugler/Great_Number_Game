from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    if 'x' not in session:
        session['x'] = random.randint(1,100)
        session['page'] = 'start'
        session['text'] = ''
        session['button'] = 'Submit'
        session['action'] = 'number'
        print(session['x'])




    return render_template('index.html')


@app.route('/number', methods=['POST'])
def numbers():
    # print(request.form['number'])
    num = int(request.form['number'])
    
    #To Low
    if num < session['x']:
        session['text'] = 'Too low!'
        session['color'] = 'red'
        print(session['page'])
    #To High
    elif num > session['x']:
        session['text'] = 'Too high!'
        session['color'] = 'red'
    #Correct
    else:
        session['text'] = str(session['x']) + ' was the number'
        session['color'] = 'green'
        session['button'] = 'Play again!'
        session['action'] = 'play-again'

    return redirect('/')

@app.route('/play-again', methods=['POST'])
def play():
    session.clear()	

    return redirect('/')


# @app.route('/')

if __name__=="__main__":
    app.run(debug=-True)