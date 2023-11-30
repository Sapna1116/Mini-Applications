import json
from difflib import get_close_matches as gcm
#gcm(val, possibilty_list, n, cutoff) #cutoff = accuracy->0.5/1/0.3

def findMeaning(word) :
    word = word.lower()   

    if word in file.keys() :
        return (file[word])

    elif word.title() in file.keys() :
        return (file[word.title()])

    elif word.upper() in file.keys() :
        return (file[word.upper()])

    elif word.capitalize() in file.keys() :
        return (file[word.capitalize()])

    elif len(gcm(word, file.keys())) > 0 : 
        x = input(f"\n\nDid you mean the word : {gcm(word, file.keys())[0]} ?  ")
        if x.lower() == "y" :
            return (file[gcm(word, file.keys())[0]])
        elif x.lower() == "n" :
            return ("\n\nNo results present for the required word in the dictionary!")
        else :
            return ("\nPlease choose from either 'y' or 'n' ")
    
    else :
        return ("\n\nNo results present for the required word in the dictionary!")
            

while (True) :
    file = json.load(open('SrcData.json'))
    ch = input("Do you want to search for a word in the dictionary? (Y/y for yes):")
    if ch.lower() == "y" :
        word = input("Enter the word you want to search for :")
        meaning = findMeaning(word)
        if type(meaning) == list :
            for item in meaning :
                print("\nMeaning : ",item, end="\n")
        else :
            print(meaning)
    else :
        print("You chose not to search any word in the dictionary!")
        print("Exiting")
        break
