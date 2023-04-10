from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en').text 
soup = BeautifulSoup(html_text,'lxml')
top_news = soup.find_all('h4',class_="gPFEn" )
print("TOP NEWS")
for headline in top_news:
    print(headline.text)
    print()   