import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

global DEBUG, VERBOSE

DEBUG = False
VERBOSE = False

def printErr(msg):
    sys.stderr.write(bcolors.FAIL + str(msg) + bcolors.ENDC + "\r\n")
    sys.stderr.flush()

def printWarn(msg):
    sys.stdout.write(bcolors.WARNING + str(msg) + bcolors.ENDC + "\r\n")
    sys.stdout.flush()

def printVerbose(msg):
    if(VERBOSE):
        sys.stdout.write(str(msg) + "\r\n")
        sys.stdout.flush()

def printDebug(msg):
    if(DEBUG):
        sys.stdout.write(str(msg) + "\r\n")
        sys.stdout.flush()

def printGreen(msg):
    sys.stdout.write(bcolors.OKGREEN + str(msg) + bcolors.ENDC + "\r\n")
    sys.stdout.flush()