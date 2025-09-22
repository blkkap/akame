import wikipedia 
import os


def getData():

   # data = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'topics.txt')
    
    with open(file_path, 'r') as f:
        topics= [line.strip() for line in f if line.strip()]
             
        try:
            for topic in topics:
                print(topic)
                data =  wikipedia.page(topic)
                print(data.title)
                dataContent = data.content
                print(dataContent)
        except wikipedia.exceptions.DisambiguationError as e:   
            print(e.options)

if __name__ == "__main__":
    
    getData()


