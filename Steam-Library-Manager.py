import os, sys
import argparse
#import pandas as pd
#import dask
#import tqdm

from modules import BaseFunctions, debug

def main():
    #print(f"helloworld from {os.name}")
    #BaseFunctions.helloWorld()

    path = os.path.join(os.getcwd(), "appmanifests")
    debug.printVerbose(f"filepath: {path}")
    
    jsonList = BaseFunctions.getManifests(path)

    print(jsonList[0])

if __name__ == "__main__":
    main()
