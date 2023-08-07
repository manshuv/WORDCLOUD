import matplotlib.pyplot as pl
from wordcloud import WordCloud, STOPWORDS

# Read text
text = open ('reviews.rtf', mode='r', encoding= 'utf-8').read()
stopwords = STOPWORDS

# Add custom stopwords
custom_stopwords = ["t", "s", "Movie","Time","Top", "Critic", "Top Critic","Many", "Full Review", "Full", "Barbie", "Review", "Original", "Score", "Film", "Jul", "Aug", "Spanish"]  # Add your custom words here
stopwords.update(custom_stopwords)


wc = WordCloud (
    background_color='white',
    stopwords=stopwords,
    height=600,
    width=400
)

wc.generate(text)

# store to file
wc.to_file('wordcloud_output.png')