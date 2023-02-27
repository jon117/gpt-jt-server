
#create a web server that listens on port 8080
#receive a string from the client

#run inference - use the GPT-JT-6B-v1 model
"""
from : https://huggingface.co/togethercomputer/GPT-JT-6B-v1
from transformers import pipeline
pipe = pipeline(model='togethercomputer/GPT-JT-6B-v1')
pipe('''"I love this!" Is it positive? A:''')
"""
#return the result to the client

import socket
import json
#from transformers import pipeline

#pipe = pipeline(model='togethercomputer/GPT-JT-6B-v1')

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 8080))
socket.listen(5)

while True:
    #accept the connection
    client, address = socket.accept()
    #receive the data
    data = client.recv(1024)
    #decode the data
    data = data.decode('utf-8')
    
    #if the data is 'exit', break the loop
    if data == 'exit':
        break
    
    print(data)
    #else run inference
    #result = pipe(data)
    result = data
    
    #send the result back to the client
    client.send(result.encode('utf-8'))
