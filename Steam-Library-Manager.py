import os, sys
import argparse
import pandas as pd
import dask
import tqdm

from modules import BaseFunctions, debug

def main():
    #print(f"helloworld from {os.name}")
    #BaseFunctions.helloWorld()

    path = os.path.join(os.getcwd(), "appmanifests")
    print(path)
    fileList = BaseFunctions.getFilesFromPath(path, ".acf")
    jsonList = []
    for file in fileList:
        parsedFile = BaseFunctions.parseManifest(file)
        if(parsedFile == None):
            debug.printErr(f"Could not parse file: {file}")
        jsonList.append(parsedFile)

if __name__ == "__main__":
    main()
