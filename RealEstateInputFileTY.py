#Name: Timothy Y
#Assignment: Real Estate and Files
#Reflection: I liked working with the csv file
#I struggled with the price list initially because I didn't do a float conversion
#I used a context manager to open the csv file because it is the safest option
#I used 3 dictionaries
#Two things I learned: 1. How to use pathlib to check for existence of a file
#2. How to extract columns from a list

import csv #import modules
from pathlib import Path


def getDataInput():
    csvData =[]
    filePath = Path("RealEstateData.csv")
    if not filePath.exists(): #data validation, checks for existence of file
        print("File does not exist")
        return csvData
    with open("RealEstateData.csv", "r") as csvfile: #open csv file as readable
        csv_reader = csv.reader(csvfile)
        next(csv_reader) #skip the heading
        for column in csv_reader:
            csvData.append(column) #populate list
    return csvData

def getMedian(price):
    price.sort()
    length = len(price)
    middle = length // 2 #finds midpoint
    if length % 2 != 0:
        median = price[middle] #indexes the median if length is odd
    else:
        median = (price[middle - 1] + price[middle]) / 2 #if length is even
    return median

def mathCalcs(value):
    value.sort()
    minimumTY = value[0] #indexes first value
    maximumTY = value[-1] #indexes last value
    totalTY = sum(value) #calculates total
    averageTY = totalTY / len(value)
    print(f"Minimum: {minimumTY:>30,.2f}\nMaximum: {maximumTY:>30,.2f}\nSum:{totalTY:>35,.2f}\nAverage: {averageTY:>30,.2f}")
def main():
    csvLst = getDataInput() #populates list with the function
    fPrice = [float(column[8]) for column in csvLst] #populates another list using the 8th column for price
    median = getMedian(fPrice) #median function which returns the median

    sCityTotalDict = {} #initialize dictionaries
    sTypeDict = {}
    sZipDict = {}

    for column in csvLst: #loop through list, extract columns
        sZip = column[2]
        propertyType = column[7]
        city = column[1]
        price = float(column[8])
        if city in sCityTotalDict:
            sCityTotalDict[city] += price #checks for duplicate keys
        else:
            sCityTotalDict[city] = price
        if propertyType in sTypeDict:
            sTypeDict[propertyType] += price
        else:
            sTypeDict[propertyType] = price
        if sZip in sZipDict:
            sZipDict[sZip] += price
        else:
            sZipDict[sZip] = price

    mathCalcs(fPrice) #math function that prints the calculations
    print(f"Median: {median:>31,.2f}") #print everything formatted all nice
    print()
    print("Summary by property type:")
    for key, propertySummary in sTypeDict.items():
        print(f"{key:15s} {propertySummary:>23,.2f}")
    print()
    print("Summary by city:")
    for key, citySummary in sCityTotalDict.items():
        print(f"{key.title():15s} {citySummary:>23,.2f}") #formatted and used title for proper capitalization
    print()
    print("Summary by zip:")
    for key, zipSummary in sZipDict.items():
        print(f"{key:15s} {zipSummary:>23,.2f}")



main()