import os, sys
import json
import io

from modules import debug


def getManifests(filePath):
    fileList = getFilesFromPath(filePath, ".acf")
    jsonList = []
    for file in fileList:
        parsedFile = parseManifest(file)
        if(parsedFile == None):
            debug.printErr(f"Could not parse file: {file}")
        jsonList.append(parsedFile)
    return jsonList


def parseManifest(filePath):
    if(not filePath.endswith(".acf")):
        return None
    
    with open(filePath, "r") as file:
        lines = file.readlines() #read all lines into an iterable

    jsonBuilder = io.StringIO("") #in memory file
    #print(jsonBuilder.read())
    prevLine = "{\n" #first line starts with open bracket
    tabcount = 1 #set indentation for human readable json
    indent = True #set indentation to true

    for line in lines: #loop through all lines in file
        lineTmp = line.strip() #remove leading and trailing whitespace
        
        if(lineTmp[0] == '"'): #if line starts with "
            if("\t" in lineTmp): #check if name and data on line
                lineTmp = lineTmp.replace("\t\t", ': ') + ",\n" #replace the two tabs between the title and variable with a colon
                
            else: #heading with multiple sub variables
                lineTmp = lineTmp + ": " #append colon

        elif(lineTmp[0] == '{'): #line starts with open bracket
            tabcount += 1 #add 1 indent
            lineTmp = lineTmp +  "\n"
            indent = False #do not add indent to previous line as bracket should be on the same line

        elif(lineTmp[0] == '}'): #line starts with close bracket
            tabcount -= 1 #decrese indent
            if((prevLine.endswith(",\n"))): #check if previous line ended with comma
                prevLine = prevLine.replace(",", "") #remove comma
            lineTmp = lineTmp +  ",\n"

        jsonBuilder.write(prevLine) #write previous line to file
        
        tmp = ""
        if(indent): #check if indents need to be added to the start of the line
            for i in range(tabcount): #loof for how many indents are requried
                tmp = tmp + "\t" #add tabs
        else: #no indent required
            indent = True #indent next loop
        prevLine = tmp + lineTmp #move current line to previous line (with indent)

    jsonBuilder.write("\t}\n}") #close off file with two curly brackets
    
    #debug  write to file
    #with open(jsonFilepath, "w") as f:
    #    print(jsonBuilder.getvalue(), file=f)
    jsonBuilder.seek(0)
    completedFile = json.load(jsonBuilder) #convert StringIO to json object
    
    return completedFile
    

#recursively get all files from"path" that end with the file extension "ext"
def getFilesFromPath(path, ext):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(path)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getFilesFromPath(fullPath, ext)
        else:
            if(entry.lower().endswith(str(ext))):
                allFiles.append(fullPath)
                
    return allFiles


def helloWorld():
   debug.printGreen("Hello World")
