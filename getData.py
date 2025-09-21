import wikipedia 
import os


def getData():

    data = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'topics.txt')
    
    file = open(file_path, 'r')
    while True:
        next_line = file.readline()
        if not next_line:
            break
        l = next_line.strip()
    data.append(l)
    print(data)  
   # try:
   #     print(l)
   #     data = wikipedia.page(l)
   #     print(data.title)
   #     dataContent = data.content
   #     print(dataContent)
   # except wikipedia.exceptions.DisambiguationError as e:
   #     print(e.options)
    


if __name__ == "__main__":
    
    getData()


