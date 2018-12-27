# FacebookWordCloud
How to make a word cloud from facebook message history

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
### ???


