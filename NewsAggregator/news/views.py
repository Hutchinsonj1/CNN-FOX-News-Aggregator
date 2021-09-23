
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.


#CNN NEWS
cnn_r = requests.get("https://www.cnn.com/us")
cnn_soup = BeautifulSoup(cnn_r.content, 'html5lib')
cnn_headings = cnn_soup.findAll('span')
cnn_headings = cnn_headings[0:]
indices_to_access = [4,6,8,10,12,14,20,24,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55]
accessed_mapping = map(cnn_headings.__getitem__, indices_to_access)
cnn_headings = list(accessed_mapping)

cnn_news = []

for cnnh in cnn_headings:
    cnn_news.append(cnnh.text)
 
#CNN NEWS 2
cnn2_r = requests.get("https://www.cnn.com/us")
cnn2_soup = BeautifulSoup(cnn2_r.content, 'html5lib')
cnn2_headings = cnn2_soup.findAll('a')
cnn2_headings = cnn2_headings[122:]
indices_to_access = [44,46]
accessed_mapping = map(cnn2_headings.__getitem__, indices_to_access)
cnn2_headings = list(accessed_mapping)

cnn_news2 = []

for cnn2h in cnn2_headings:
    cnn_news2.append(cnn2h.text)  

#CNN NEWS 3
cnn3_r = requests.get("https://www.cnn.com/specials/us/crime-and-justice")
cnn3_soup = BeautifulSoup(cnn3_r.content, 'html5lib')
cnn3_headings = cnn3_soup.findAll('span')
cnn3_headings = cnn3_headings[3:450:2]

cnn_news3 = []

for cnn3h in cnn3_headings:
    cnn_news3.append(cnn3h.text) 



  
#FOX NEWS
f_r = requests.get("https://www.foxnews.com/?page=42364&external=3829093.proteus.fma")
f_soup = BeautifulSoup(f_r.content, 'html5lib')
f_headings = f_soup.findAll('h2')
f_headings = f_headings[2:]
fox_news = []

for fh in f_headings:
    fox_news.append(fh.text)

 

def index(req):

    return render(req, 'news/index.html', {'cnn_news':cnn_news,'cnn_news2':cnn_news2,'cnn_news3':cnn_news3, 'fox_news':fox_news})

 


  
      