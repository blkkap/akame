import wikipedia 
import os


#print(wikipedia.search("neural network"))
 
# NN = wikipedia.page("neural network(machine learning)")

# print(NN.content)




def getData():
    # data = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'topics.txt')
    
    #with open(file_path) as f:
       # lines = [line.rstrip('\n') for line in f]
            
        #print(lines)
    file = open(file_path, 'r')
    while True:
        next_line = file.readline()

        if not next_line:
            break
        l = next_line.strip()
        print(l)


if __name__ == "__main__":
    
    getData()



