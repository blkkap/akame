import requests
from bs4 import BeautifulSoup
import os



def getData():

    with open("topics.txt", 'r', encoding='UTF-8') as file:
        while line := file.readline():
           # l = line.rstrip()

            url = line.rstrip()
    
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
   
    title = soup.find(id="firstHeading").text
   # print(title)

    paragraphs = soup.select("p")
    for p in paragraphs:
        #print(p.text)

        p_text = '\n'.join(para.text for para in paragraphs[:])
    with open(f'data/{title}', 'w', encoding='utf-8') as file:
        file.write(p_text)    
    
    


if __name__ == "__main__":
    getData()
    


