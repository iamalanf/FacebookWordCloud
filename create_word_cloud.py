'''
This file  takes a 'message_content.txt' file and creates a 'wordcloud.png'
file

TODO: put below in functions!
'''

# Import matplotlib for rendering
import matplotlib.pyplot as plt
# import wordcloud things
from wordcloud import WordCloud, STOPWORDS

# Get stopwords as as set (no repeats)
stopwords = set(STOPWORDS)

# Open message content for reading
filename = open('message_content.txt', 'r', encoding="utf-8")
# Print if sucessful
print("Found file %s" % (filename))

# Create master string
strings = ''

# Go through every line in file and append line to master string 
for line in filename:
    strings = strings + ' ' + line
    
# Fix to reduce white space
strings = ' '.join(strings.split())
    
# Set wordcloud parameters
# (trying to get suitable for A4 paper)
wc = WordCloud(background_color='white',
                      stopwords=stopwords,
                      width=1000, height=595, #pixels
                      mask=None,
                      max_words=1000,
                      max_font_size=40, 
                      random_state=42)

# Generate the wordclous using the above parameters and the master string
wc.generate(strings)

# Set the size of the figure (again trying to get suitable for a4 paper)
fig = plt.figure(figsize=(14, 9))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.figure()
fig.savefig("wordcloud.png", dpi=100,
            papertype='a4', orientation='portrait')
