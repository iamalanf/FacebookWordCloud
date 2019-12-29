import sys, getopt # For command line arguments
# Local:
import parse_facebook_json as jsonParser
import create_word_cloud as wordCloud

# Command line interpreation
def main(argv):

    __printWelcome()

    inputfile = ""
    outputfile = ""
    parseJson = True
    try:
        opts, args = getopt.getopt(argv,"hi:o:w",["inputFile=","outputFile=","wcOnly"])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
   
    for opt, arg in opts:
        if opt == "-h":
            print("test.py -i --inputFile <inputfile> -o --outputFile <outputfile> -w --wcOnly (only print out wc do not parse json. Note json file needs to be parsed at some point)")
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            inputfile = arg
        elif opt in ("-o", "--outputFile"):
            outputfile = arg
        elif opt in ("-w", "--wcOnly"):
            print("--wcOnly given not parsing json")
            parseJson = False

    # Check files set TODO: check correct type in future
    inputfile, outputfile = __checkFiles(inputfile, outputfile)

    if(parseJson):
        jsonParser.parseFacebookJson(inputfile, outputfile)
    wordCloud.createWordCloud(inputfile, outputfile)

    __printComplete()


def __printWelcome():
    print("Running facebook wordcloud")

def __printComplete():
    print("\nFinished!")

# TODO: would prefer in sep file
def __checkFiles(inputFileName, outputFileName):
    if(inputFileName == ""):
        print("Error: input file not set. Please set a json input file using command line arg -i or --inputFile")
        sys.exit(1) 
    if(outputFileName == ""):
        print("Warning: output file not set. Default to output.png Set an output file using command line arg -o or --outputFile. Extension will be png by default")
        outputFileName = "outputFile"

    print("Input file is: %s" % inputFileName)
    print("Output file is: %s" % outputFileName)    

    return inputFileName, outputFileName

if __name__ == "__main__":
    main(sys.argv[1:])
