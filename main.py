
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
def summarize():

    #For url, I have to specify a start and end point. 
    url = utext.get('1.0',"END").strip()
    
    article = Article(url)

    article.download()

    article.parse()

    article.nlp()

#config is required for the user to not be able to make changes
#and we have to apply this process separately to get rid of each column expressed with the print below.  
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
# In case of changing the content, we will want to delete everything there first.
# this way sensitivity is made available for analysis
    title.delete('1.0', "END")
    title.insert('1.0', article.title)
    
    author.delete('1.0', "END")
    author.insert('1.0', article.authors)
    
    publication.delete('1.0', "END")
    publication.insert('1.0', article.publish_date)
    
    summary.delete('1.0', "END")
    summary.insert('1.0', article.summary)
     
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', "END")    
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    
    
#For "disabled" on content change     
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

#tkinter
root = tk.Tk()
root.title('News Summerizer')
root.geometry('1200x600')

# We will define the properties of the headers that we will tag between root.mainloop () and root.
tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)

# We're going to do a configuration here. "Disable" for the user not to put anything other than the url in the box and "bg" for the background color.
title.config(state='disabled', bg='#dddddd')

#We pack it with pack() and complete it.
title.pack()


#Same procedures for authors tab
alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

#Same procedures for publication date tab
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

#Same procedures for summary tab
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

#Same procedures for sentiment analysis
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

#for the url to be entered by the user
ulabel = tk.Label(root, text="Enter URL")
ulabel.pack()
# In order not to write a url for the 2nd time, we named it differently 'utext' as it should not interfere with the other variable.
utext = tk.Text(root, height=1, width=140)
utext.pack()

#Now let's add a button for the summary
#We will connect command with def. 
bt =tk.Button(root, text='Summarize', command=summarize)
bt.pack()

root.mainloop()
