import os, sys

from modules import debug




def parseManifest(filePath):
    if(not filePath.endswith(".acf")):
        return None
    
    

    return "PLACEHOLDER"
    

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
