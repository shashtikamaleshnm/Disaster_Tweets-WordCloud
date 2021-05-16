#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS


# In[2]:


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


# In[3]:


train.head()


# In[4]:


test.head()


# In[5]:


train.shape


# In[6]:


test.shape


# In[7]:


STOPWORDS.add('https')

def plot_word(text):
    
    comment_words = ' '
    stopwords = set(STOPWORDS)
    
    for val in text:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        
        for words in tokens:
            comment_words = comment_words + words + ' '
    
    wordcloud = WordCloud(
        width = 5000,
        height = 4000,
        background_color = 'black',
        stopwords = stopwords,
        min_font_size = 10
    ).generate(comment_words)
    
    plt.figure(figsize = (12, 12), facecolor = 'k', edgecolor = 'k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    
    plt.show()


# In[8]:


text = train.text.values
plot_word(text)

