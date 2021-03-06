from random import randint
import time
from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/main',methods=["GET","POST"])
def homepage():
    x = randint(10,99)
    y = randint(10,99)
    if request.method=='GET':
        return render_template('main.html',x=x,y=y)
    else:
        if int(request.form["x"])+int(request.form["y"])==int(request.form["result"]):
            msg = 'Correct'
        else:
            msg = 'Incorrect'

        if msg=='Correct':
            color1 = 'text-success'
        else:
            color1 = 'text-danger'
        return render_template('main.html',x=x,y=y,msg=msg,color1=color1)
def getOutput():
    start_time = time.time()
    x = randint(10,100)
    y  = randint(10,100)
    time_taken = int(time.time() - start_time)
    output = x+y
    return x,y,output,time_taken


@app.route('/test')    #additional endpoint for testing purpose
def test(): 
    return render_template('footer.html')

app.run()
