# Author: Dylan Eckstein. APR 2019. dylaneckstein@hotmail.com
# Purpose: Create a function to decide if an acronym is valid or invalid for a product name

def p(msg) :
    print(msg)

# return:bool, acronym:str, productName:list[str]
# Returns True if acronym is valid and False if acronym is invalid
# Checks once for each method
# The first method iterates through the Product Name strings and removes the first letter of the acronym if there is a match
# The second method is the same but it will skip to the next word if the next acronym letter is within the next word
# Both of these methods have cracks but the acronym only has to be valid for one for the overall answer to be True
def isValid(acronym, productName):

    # The main check function
    def check(acronym, productName, skipForward=False):
        if len(acronym) < len(productName):  # Length check first
            return False
        acronym = acronym.lower()  # Lowercase everything to match case
        for x in range(0, len(productName)):
            productName[x] = productName[x].lower()
        for j in range(0, len(productName)):  # For each string in productName
            currentString = productName[j]
            acronymStartLen = len(acronym)
            for i in range(0, len(currentString)):  # For each letter in the current string
                if currentString[i] == acronym[0]:  # Main check
                    if len(acronym) > 1:  # Remove the front letter of the acronym if possible
                        acronym = acronym[1:]
                        if j != len(productName) - 1 and skipForward is True:  # If we are skipping forward then do so
                            if acronym[0] in productName[j+1]:
                                break
                    else:  # If that was the last character to check in the acronym
                        if j == len(productName) - 1:  # If we are in the last string
                            return True
                        else:
                            return False
            if len(acronym) == acronymStartLen:  # If the acronym hasn't been altered for the current string's iteration
                return False
        return False

    # This is the call middleman. Only one check has to be valid for the overall answer to be True
    return check(acronym, productName) or check(acronym, productName, skipForward=True)



# Our "main"
valid = ['GIZTK3', 'GZT3', 'GISEE0']
invalid = ['GZT3k', 'GZT', 'GZTK', 'BLAH']
p("Alleged Valids;")
for x in valid:
    p(isValid(x, ["GISInc", "Zombie", "Tracker", "3000"]))
p("\nAlleged Invalids;")
for x in invalid:
    p(isValid(x, ["Google", "Search", "Engine"]))

valid = ['GOOSE', 'GEANIE', 'OOSN', 'LEACHE', 'OOGLEE', 'GOOSEEE', 'GGSEE', 'GGSE']
invalid = ['SGE', 'GEANIEOOSN', 'OGGLEE', 'GGG', 'GGSEA']
p("\n\nAlleged Valids;")
for x in valid:
    p(isValid(x, ["Google", "Search", "Engine"]))
p("\nAlleged Invalids;")
for x in invalid:
    p(isValid(x, ["Google", "Search", "Engine"]))



