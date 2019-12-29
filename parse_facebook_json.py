'''
This file  takes a json file exported from facebook and creates two files:
 > 'message_content.txt' - containing all message text content, for use in
   creating a wordcloud
 > 'messages.csv' - containing all message information in csv format, for
    use data analysis

TODO: put below in functions!
'''

# Load required modules
import json # json for reading the json file downloaded from Facebook
import pandas as pd # pandas for exporting the data to csv (for analysis)

class parseFacebookJson:
    def __init__(self, inputFileName, outputFileName):
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName + '.txt' # txt file
        self.messageEntries = self.__openFile()
        self.outputFile = self.__createOutputFile()
        self.__processContent()
        self.__closeOutputFile()

    def __openFile(self):
        # Open the json file for reading
        with open(self.inputFileName, 'r') as f:
            my_dict = json.load(f)
        # my_dict is a dictionary. Get all entries corresponding to 
        # the key 'messages' this will be the content for the wordcloud
        return my_dict.get('messages')

    def __createOutputFile(self):
        # Open a file which will be used to write the message content to 
        file = open(self.outputFileName, 'w', encoding="utf-8")
        return file

    def __closeOutputFile(self):
        self.outputFile.close()

    def __processContent(self):
        #Create new pandas dataframe
        df = pd.DataFrame()

        # Counter for number of message entries
        count = 0

        # Go through each entry
        for entry in self.messageEntries:
            # Get the message content from the inner dictionary
            # ('sender_name', 'timestamp_ms', 'type', 'photos' etc fields also exist)
            message = entry.get('content')
            
            # Write the content to output file (have put spaces either side to ensure 
            # that words do not merge)
            self.outputFile.write(' %s \n' % (message))
            
            # Increment the counter
            count = count + 1
            
            # Convert entry to temporary dataframe
            df_temp = pd.DataFrame([entry], columns=entry.keys())
            # Append the temporary df to the master df
            df = df.append(df_temp, ignore_index = True)
            
            # Print how may messages have been processed
            print('\rCount %i ' % (count), end='')
    
        # Export the  dataframe as csv (csv will be handy for analysis)
        df.to_csv('messages.csv')

