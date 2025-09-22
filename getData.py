# import wikipedia 
import requests
from bs4 import BeautifulSoup
import os


def getData():
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    print(response.status_code)
    
    soup = BeautifulSoup(response.content, 'html.parser')
   
    title = soup.find(id="firstHeading").text
    print(title)

    paragraphs = soup.select("p")
    for p in paragraphs:
        print(p.text)
    
    


if __name__ == "__main__":
    
    getData()


