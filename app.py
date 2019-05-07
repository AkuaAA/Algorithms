#Created a simple flask application

from flask import Flask
import time
import random
import numpy
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
    list = numpy.random.random_integers(1, 1000, x)
    #print(list)
    list.sort()
    time_now = time.time()
    final_time = time_now - current_time
    return str(final_time) #converts into a string

@app.route("/reverse")
def reverse_time():
    current_time = time.time() #method for getting runtime
    list = ['zero', 'one', 'two', 'three']
    list.reverse() #method for reverse
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
