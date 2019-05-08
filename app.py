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

#quadratic graph solution O(N2)
@app.route("/dupe")
def dupe():
    list = [1, 2, 1]
    dupes = []
    current_time = time.time()
    for i in range(0, (len(list) -1), +1):
        count = 0
        while count < len(list):
            if word != count:
                if list[i] == list[count]:
                    dupe.append(list[i])
                    count += 1
                else:
                    count += 1
            else:
                count += 1
    time_now = time.time()
    final_time = time_now - current_time
    print(dupes)
    return "yay"



#linear graph solution - O(N)
@app.route("/dupe2")
def dupe2():
    co_ords = []
    for k in range (1, 1001, +50):
        arr = [1, 2, 3, 2]
        arr_size = len(arr)
        current_time = time.time()
        for i in range(0, arr_size):
            if arr[abs(arr[i])] >= 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
                print (abs(arr[i]), end = " ")
            time_now = time.time()
            final_time = time_now - current_time
            co_ords.append([4, final_time])
            print("The repeating elements are: ")
    return "yay"

#visual representation for what is happening in the loop
#The repeating elements are:
# loop 0
#[1, -2, 3, 2]
# loop 1
#[1, -2, -3, 2]
#loop 2
#[1, -2, -3, -2]
#loop 3
#2 [1, -2, -3, -2] #duplicate found!

@app.route("/graph")
def graph():
    return render_template("graph.html")


if __name__ == "__main__":
    app.run()
