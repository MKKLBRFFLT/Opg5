from socket import *
import json

# Variable
serverName = 'localhost'
serverPort = 7

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Choose an operation:")
print("R. Random")
print("A. Add")
print("S. Subtract")

while True:
    choice = input("What would you like to do? (Random(R)/Add(A)/Subtract(S)): ").upper()

    if choice in ['R', 'A', 'S']:
        break
    else:
        print("Invalid choice. Please try again.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Opretter dict object til brug med JSON
data = {
    "function": choice,
    "Number1": num1,
    "Number2": num2
}

data_json = json.dumps(data)


clientSocket.send(data_json.encode())

dataBack = clientSocket.recv(2048)
sentenceBack_json = dataBack.decode()

response_data = json.loads(sentenceBack_json)

print('Received text:', response_data)
clientSocket.close()
