#importing the csv file and copying
import csv
import copy

#the dictionary of my vehicle
myVehicle = {
        "vin" : "<empty>",
        "make" : "<empty>" ,
        "model" : "<empty>" ,
        "year" : 0,
        "range" : 0,
        "topSpeed" : 0,
        "zeroSixty" : 0.0,
        "mileage" : 0
    }
#checking the key values for the my vehicle dictionary
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))