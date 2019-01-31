#Author: Jayendra Matarage
#Title: Distance Finder
#Date : 31, Jan, 2019
#import csv
import pandas as pd

class Getdata:

    def readData(self,position_one,position_two):
        CSVDATA = "citiesdata.csv"
        data = pd.read_csv(CSVDATA, header=None)

        position_one_data = data[data[0] == position_one].values
        position_two_data = data[data[0] == position_two].values

        return [[position_one_data],[position_two_data]]
