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
#creating a new category (the category below is empty)
myInventoryList = []
#opening the csv file that was created with the command below (since my csv file is not a root file but in a folder i used the ('copy relative path/the csv file name))
with open('LAB1/car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  #reading the csv file
    lineCount = 0  
    for row in csvReader:
            if lineCount == 0: #((== two is for comparison while =one is for assigning))
                print(f'Column names are: {", ".join(row)}')  
                lineCount += 1  
            else:  
                print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
                currentVehicle = copy.deepcopy(myVehicle)  
                currentVehicle["vin"] = row[0]  
                currentVehicle["make"] = row[1]  
                currentVehicle["model"] = row[2]  
                currentVehicle["year"] = row[3]  
                currentVehicle["range"] = row[4]  
                currentVehicle["topSpeed"] = row[5]  
                currentVehicle["zeroSixty"] = row[6]  
                currentVehicle["mileage"] = row[7]  
                myInventoryList.append(currentVehicle)  
                lineCount += 1  
    print(f'Processed {lineCount} lines.')