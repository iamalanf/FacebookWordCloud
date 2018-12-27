# FacebookWordCloud
How to make a word cloud from facebook message history. A perfect cheap card/gift for a new years eve card or anniversary. 

This focuses more on how to get the data from Facebook at the moment. The Python code provided works, but if it is to be taken further will need re-formatting. 

Data-analysis of messages will also be updloaded in the future. 

## Step One
### Download the history from Facebook
1. Log into Facebook
2. In the dropdown on the main panel click on the arrow down and select settings. 

![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture1.png)

![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture2.png)

3. Select "Your Facebook information" from the side panel on the left. 
![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture3.png)

4. Select "View" on the left of "Download your information"
![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture4.png)

5. Wow they collect all sorts of information. Here we want messages; to select just messages quickly toggle "Deselect all" and then check the box next to messages. 
* Make sure to change the format to json! This format is alot easier for Python (what we will be using later) to parse. 
* Set the date range as your wish. Note that if you do use Facebook alot file sizes can approach the GB and may take an hour to process/download. 
* Set the media quality to low. We are interested in a wordcloud so the media is not of interest. This will be things such as gifs, photos, videos, attachements etc...
* When ready select "Create File"
![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture5.png)

6. The tab should switch over to "Available files", if it does not automatically then click there yourself. Here the requested file is shown along with the date of creation. This file will be listed as pending whilst Facebook readies the data. This may take a while depending on the amount of data that is being fetched. All 4GB request from me (all messages ever) took about 2 hours. A notification and email will be send when the file is ready so feel free to crack on with your day. <br> When the file is ready click on download; your Facebook password may be requested in order to start the download. 
![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture6.png)

7. Extract the contents of the downloaded zip file to a directory of your choice. I would suggest your working directory for the Python ode to come, but as long as the path is easily available it should not matter. 

## Step Two
### Finding the json file

8. Extracting the folder should create a folder called something like "facebook-YOURUSERNAME". The second level should be the requested fields. If you are following this tutorial to the letter only a "messages" folder should be visible as that is the only information that was asked for. 

9. Enter the "messages" folder. Several folders may exist here, we are interested in the "inbox" folder for the wordcloud. Other folders may exist such as "stickers_used", "archived_threads" etc.. the content of these will not be used for the wordcloud.

10. Enter the "inbox" folder. Here all message threads between you and other facebook users can be seen in seperate folders. Enter the folder corresponding to the person/people you wish to visualise with the wordcloud. 

11. Copy the "message.json" file to your working directory for the Python analysis to come. Or make sure you have the path to the file handy. gifs, photos and videos directories may also be seen within the conversation folder. These will not be included within the wordcloud. 

## Bonus Step
### Lets have a look at the structure of the json file

* There are several top level keys; "participants", "messages", "title", "is_still_participant", "thread_type", "thread_path". We are interested in "messages". 
* Keys in the message leaf are "sender_name", "timestamp_ms", "content" and "type". For the wordcloud we are interested in the "content" field as here what the participants has typed is stored. This is what will be used for the wordcloud. 
* If you want to visualise the json file, I suggest Visual Studio Code as it has some nice json plug-ins. 
![alt text](https://github.com/DoomedBunny/FacebookWordCloud/blob/master/images/Picture7.png)

## Step Four
### Grabbing the content from the json file

12. The Python file "parse_facebook_json.py" at the top level of this GitHub repositry have what we need to get the content out of the json files. I will not go into detail on how the Python script works here. Hopefully the comments in the code will suffice! 
* Assuming that the json file is called "message.json" and exists in the same directory as "parse_facebook_json.py" (alternatively enter the path to the json file within the Python script. 
* Make sure you have the required Python dependencies. A "requirements.txt" is available at the top level of this repositry to use run : "pip install -r requirements.txt". (I am using Anaconda which has many of the required dependcies already and would suggest!). I have gone overkill with the requirements as I created this when doing some analysis and data visualisation.. apologies!
* Run "parse_facebook_json.py". This may take a while depending upon the size of the file. A count should be printed to console. Two files should be output:
** "message_content.txt" - this is the content of all text messages send. It is this that will be used to create to wordcloud. 
** "messages.csv" - stores data on all messages. This can be used for data analysis (COMING SOON!) (If you are comfortable with pandas read this in with pd.read_csv and have a play). 

## Step Five
#### Creating the wordcloud

13. Finally, we can create the wordcloud! The Python file "create_word_cloud.py" is used for this purpose. This is kept seperate from the "parse_facebook_json.py" at present as this file runs alot quicker. For quickly resizing and crudely running Python a seperate file is how I have worked thus far. (Could put in main function and reference classes/parsing in future). 
* Run "parse_facebook_json.py" and a "wordcloud.png" file should be created. 
** I have tried to get the output image to be suitable for A4 paper output. Feel free to play with the parameters to tweek to your liking. (Please let me know if you find a better way of doing this!).
* Further work may need doing on removing repeat words surrounded by whitespace and that included when pictures etc are sent. But nonetheless, for a length visualisation this should provide a good insight into conversation history!

## Bonus Step
#### Artsy wordcloud
Masks can be appled to the wordcloud to contrain the image within certain shapes. Checkout the links below on how to do this:
* https://amueller.github.io/word_cloud/auto_examples/masked.html
* https://medium.com/@dudsdu/an-example-of-word-cloud-with-mask-4cbbd699fb14
For stencils checkout:
* stencilry (but this has been down for a while now so will try provide an alterative in future)


