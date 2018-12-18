import numpy as np # linear algebra
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS


stopwords = set(STOPWORDS)
filename = open('message_content.txt', 'r', encoding="utf-8")
print("Found file %s" % (filename))

strings = ''
for line in filename:
    strings = strings + ' ' + line
    
# Reduce white space
strings = ' '.join(strings.split())
    
#data = pd.read_csv("../input/most_backed.csv")

wc = WordCloud(background_color='white',
                      stopwords=stopwords,
                      width=1000, height=595, #pixels
                      mask=None,
                      max_words=1000,
                      max_font_size=40, 
                      random_state=42)

wc.generate(strings)
#).generate(str(data['title']))

fig = plt.figure(figsize=(14, 9))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.figure()
fig.savefig("word1.png", dpi=100,
            papertype='a4', orientation='portrait')
