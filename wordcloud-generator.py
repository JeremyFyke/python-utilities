# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 07:11:34 2020

@author: FykeJ

This utility loads a csv file into a Pandas dataframe, reads a column from this file,
and adds all words from this file into a wordcloud.

Notes:
    -Not sure if this works with multiword items.
"""

import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

fname="test-impacts.csv"
column_name="IMPACT"

df=pd.read_csv()
df[[column_name]].head()
text=''
for val in df.IMPACT:
    val=str(val)
    text += val+' '

word_cloud=WordCloud(background_color="white", 
           width=1000,
           height=500).generate(text)

plt.imshow(word_cloud,
          interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file("wordcloud.png")

