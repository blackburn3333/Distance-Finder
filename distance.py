# Author: Jayendra Matarage
# Title: Distance Finder
# Date : 31, Jan, 2019
import math


class Distance:
    def generateDistance(self, firstPointData, secondPointData):
        EARTH_RADIUS = 6373.0

        latitude_one = math.radians(float(firstPointData[1]))
        longitude_one = math.radians(float(firstPointData[2]))

        latitude_two = math.radians(float(secondPointData[1]))
        longitude_two = math.radians(float(firstPointData[2]))

        x = latitude_two - latitude_one
        y = longitude_two - longitude_one

        a = math.sin(x / 2) ** 2 + math.cos(latitude_one) * math.cos(longitude_two) * math.sin(y / 2) ** 2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return  round(EARTH_RADIUS * c,1)

