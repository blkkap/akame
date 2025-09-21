import wikipedia 

print(wikipedia.search("neural network"))
 
NN = wikipedia.page("neural network(machine learning)")

print(NN.content)

