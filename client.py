
#connect to server on localhost:8080
#ask the user for input
#send the input to the server
#receive the result from the server
#display the result

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 8080))
print("connected to server")

print("testing connection...")
socket.send("test".encode('utf-8'))
result = socket.recv(1024)
result = result.decode('utf-8')
if result == "test":
    print("connection successful")

while True:
    #ask the user for input
    data = input('Ask GPT a question: ')
    
    #if the data is 'exit', break the loop
    if data == 'exit':
        break
    
    #send the data to the server
    socket.send(data.encode('utf-8'))
    
    #receive the result from the server
    result = socket.recv(1024)
    
    #decode the result
    result = result.decode('utf-8')
    
    #display the result
    print("response: " + str(result))