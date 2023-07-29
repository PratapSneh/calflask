'''
from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Welcome to home page</p>"

@app.route('/welcome')
def welcome():
    return "Welcome to the flask tutorial"

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

'''

from flask import Flask,render_template

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to Flask"

@obj.rout('/cal',method=["GET"])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    else:
        result=number1-number2
    return result
    



print(__name__)

if __name__=='__main__':
    obj.run()