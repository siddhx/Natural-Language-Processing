import urllib.request
import nltk
from bs4 import BeautifulSoup
import re
import operator

# response = urllib.request.urlopen('http://python.org/')
# response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Machine_learning')
# response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Pattern_recognition')

html = response.read()

html_soup = BeautifulSoup(html, "lxml")
# print(html_soup.get_text())

tokens = [token for token in html_soup.get_text().split()]
# tokens = re.split('\W+',html_soup.get_text())

freq_dis = {}
for token in tokens:
    if token in freq_dis:
        freq_dis[token] += 1
    else:
        freq_dis[token] = 1

# We want to sort this dictionary on values ( freq in this case )

# sorted_freq_dist = sorted(freq_dis.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_freq_dist[:25])

Freq_dist_nltk = nltk.FreqDist(tokens)
# print(Freq_dist_nltk)

#Sorting the Freq_dist_nltk

sorted_Freq_dist_nltk = sorted(Freq_dist_nltk.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_Freq_dist_nltk)

# for key,value in sorted_Freq_dist_nltk:
#     print(str(key)+':'+str(value))

# Freq_dist_nltk.plot(50, cumulative=False)

stopwords = [word.strip().lower() for word in open("./english.stop.txt")]

clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stopwords)]

Freq_dist_nltk = nltk.FreqDist(clean_tokens)

# Freq_dist_nltk.plot(50, cumulative=False)
sorted_Freq_dist_nltk = sorted(Freq_dist_nltk.items(), key=operator.itemgetter(1), reverse=True)

for key,value in sorted_Freq_dist_nltk:
    print(str(key)+':'+str(value))

Freq_dist_nltk.plot(50, cumulative=False)
