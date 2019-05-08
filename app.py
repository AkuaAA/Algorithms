#Created a simple flask application

from flask import Flask, render_template,request
from flask import jsonify
import json
import time
import random
import numpy
import plotly
from random import randint


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

@app.route("/myshuffle")
def my_shuffle():
    co_ord = []
    current_time = time.time()
    for k in range (1,1001, +50): #creating array list
        list = numpy.random.random_integers(1, 100, k) #generates random array
        current_time = time.time()
        print(list)
        for i in range((len(list)-1), 0, -1): #for loop that specifies how many elements are actually in the array that you want to work on
            a = random.randint(0, len(list)-1) #generates number
            list[i],list[a] = list[a],list[i] # syntax for swapping the numbers
        print(list) #print to visualise the code
        time_now = time.time()
        final_time = time_now - current_time
        co_ord.append([k,final_time]) #creates the format of the x and y cordinates the way json likes it
    return jsonify(co_ord) #created to visualise graph

@app.route("/graph")
def graph():
    return render_template("graph.html")


if __name__ == "__main__":
    app.run()
