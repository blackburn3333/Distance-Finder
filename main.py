#Author: Jayendra Matarage
#Title: Distance Finder
#Date : 31, Jan, 2019

from getdata import Getdata
from distance import Distance

getdata = Getdata()
distanceCal = Distance()


def main():
    print("---------------------------------")
    print("|\t\tDISTANCE FINDER\t\t|")
    print("---------------------------------")

    point_one = input("Enter first position: ")
    while point_one == '':
        point_one = input("Re Enter first position: ")

    check = getdata.checkPoing(point_one)
    while len(check) == 0:
        print("No position data")
        point_one = input("Re Enter first position: ")
        check = getdata.checkPoing(point_one)

    point_two = input("Enter second position: ")
    while point_two == '':
        point_two = input("Re Enter second position: ")
    check = getdata.checkPoing(point_two)
    while len(check) == 0:
        print("No position data")
        point_two = input("Re Enter second position: ")
        check = getdata.checkPoing(point_two)

    data = getdata.readData(point_one,point_two)

    print("|\t First Point: " + data[0][0][0][0])
    print("|\t Second Point: " + data[1][0][0][0])
    print("---------------------------------")
    distance = distanceCal.generateDistance(data[0][0][0],data[1][0][0])
    print("Approximate distance of " + data[0][0][0][0] + " to " +   data[1][0][0][0] + " is " + str(distance) + " km")

    choice = input("Find distance again ? (Y)es or (N)o : ")

    if(choice == "Y"):
        main()

if __name__ == '__main__':
    main()
