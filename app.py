#Created a simple flask application

from flask import Flask
import time
import random
import numpy
import plotly
from random import randint

#created global variable
global x_cord
x_cord =[]

global y_cord
y_cord =[]

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/last")
def last_time():
    current_time = time.time() #method for getting runtime
    last =  ['zero', 'one', 'two', 'three']
    last[-1] #gets the last array
    time_now = time.time()
    final_time = time_now - current_time
    return str(final_time) #converts into a string

@app.route("/sort")
def sort_time():
    current_time = time.time() #method for getting runtime
    x = randint(1, 1000)
    x_cord.append(x)
    list = numpy.random.random_integers(1, 1000, x)
    #print(list)
    list.sort()
    print(x_cord)
    time_now = time.time()
    final_time = time_now - current_time
    y_cord.append(final_time)
    print(y_cord)
    return str(final_time) #converts into a string

@app.route("/reverse")
def reverse_time():
    current_time = time.time() #method for getting runtime
    list = ['zero', 'one', 'two', 'three']
    list[:] = list[::-1] #method for reverse
    time_now = time.time()
    final_time = time_now - current_time
    return str(final_time) #converts into a string

@app.route("/shuffle")
def shuffle_time():
    current_time = time.time() #method for getting runtime
    list = ['zero', 'one', 'two', 'three']
    random.shuffle(list) #calls the random method
    time_now = time.time()
    final_time = time_now - current_time
    return str(final_time) #converts into a string


if __name__ == "__main__":
    app.run()
