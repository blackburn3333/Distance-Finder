#Author: Jayendra Matarage
#Title: Distance Finder
#Date : 31, Jan, 2019

from getdata import Getdata
from distance import Distance

getdata = Getdata()
distance = Distance()

if __name__ == '__main__':

    print("---------------------------------")
    print("|\t\tDISTANCE FINDER\t\t|")
    print("---------------------------------")

    point_one = input("Enter first position: ")
    point_two = input("Enter second position: ")

    data = getdata.readData(point_one,point_two)

    print("|\t First Point: " + data[0][0][0][0])
    print("|\t First Point: " + data[1][0][0][0])
    print("---------------------------------")
    distance = distance.generateDistance(data[0][0][0],data[1][0][0])
    print("Approximate distance of " + data[0][0][0][0] + " to " +   data[1][0][0][0] + " is " + str(distance) + " km")

