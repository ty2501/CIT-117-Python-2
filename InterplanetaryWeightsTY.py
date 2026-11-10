#Name: Tim Y
#Assignment: Planetary Weights Dictionaries
#Reflection: What I liked about the assignment? Pickling to save data to a file.
#What I struggled with? The nested for loops
#How did I like working with dictionary and pickling concepts? It was very interesting to utilize pickling with a saved data file. Definitely a challenging project.
#2 Things I learned on this assignment:
#1. How to utilize dictionaries to access values by keys
#2. How to use data validation to confirm the existence of a file

import pickle

dictPlanetWeights = {  # the planets = key, the value = weight factor
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 0.93,
    "Uranus": 0.92,
    "Neptune": 1.12,
    "Pluto": 0.066,

}
def PromptForInput(sPrompt): #data validation function for the weight
    while True:
        try:
            inputTY = float(input(sPrompt))
            if inputTY > 0:
                return inputTY
            else:
                print("Enter a number >0")
        except ValueError:
            print("Enter a numeric value")

def SaveFile(dictionary): #save file function
    with open('tyPlanetaryWeights.db', 'wb') as output_file: #open the file as writable using context manager
        pickle.dump(dictionary, output_file) #save and append the calculated weights within the dictionary to the output data file
    print("History saved.")

def main():

    dictPlanetHistory = {} #initialize history dictionary
    eof = False #data validation loop checks for existence of file
    try:
        with open('tyPlanetaryWeights.db', 'rb') as input_file: #opens the data file as read only
            while not eof:
                try:
                    dictPlanetHistory = pickle.load(input_file) #attempts to load in the data from the data file
                except EOFError: #if file is empty, skip
                    eof = True
    except FileNotFoundError: #if file does not exist, continue
        pass
    sHistoryTY = input("Would you like to see the history? Y/N: ").upper()
    if sHistoryTY == "Y":
            if not dictPlanetHistory:
                print("Database is empty. Add some stuff!") #checks to see if there is data in the dictionary
            else:
                for name, weights in dictPlanetHistory.items(): #prints the data using a for loop to iterate by key
                    print(f"Name : {name}")
                    for planet, weight in weights.items():
                        print(f"Planet: {planet:<10} {weight:10.2f} lbs") #prints the calculated results formatted
    else:
        print("Skipping")
    while True:
        sNameTY = input("Enter a unique name (ENTER key to quit): ").capitalize().strip()
        if sNameTY == "": #empty string breaks the loop
            break
        if sNameTY in dictPlanetHistory: #checks for unique name
            print(f"{sNameTY} is already in the history file. Enter a unique name.")
            continue

        sEarthWeightTY = PromptForInput("Enter your Earth weight: ") #user's weight input with data validation
        dictPersonWeights = {} #initialize the person weights dictionary
        print(f"{sNameTY}, here are your weights on our Solar System's planets!")
        for planet, weight in dictPlanetWeights.items():
            calculatedWeight = weight * sEarthWeightTY #calculates persons weight on each planet
            dictPersonWeights[planet] = calculatedWeight #saves the calculations to the dictionary
            print(f"Planet: {planet:<10} Weight: {calculatedWeight:10.2f} lbs" ) #formatted all nice :)
        print() #empty string as a seperator
        dictPlanetHistory[sNameTY] = dictPersonWeights #uses the previous dictionary to save to the history dictionary
    if dictPlanetHistory:
        SaveFile(dictPlanetHistory) #save file

main()