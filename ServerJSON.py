import socket
import threading
import random
import json

def HandleClient(connectionSocket, address):
    print('Address:', address)

    data = connectionSocket.recv(2048)
    json_data = data.decode()

    try:
        received_data = json.loads(json_data)

        function = received_data["function"].upper()
        num1 = received_data["Number1"]
        num2 = received_data["Number2"]

        if function == "R" or function == "RANDOM":
            result = random.randint(num1, num2)
        elif function == "A" or function == "ADD":
            result = num1 + num2
        elif function == "S" or function == "SUBTRACT":
            result = num1 - num2
        else:
            result = "Invalid input"

        # Svaret til klienten oprettes som en dict
        response_data = {
            "result": result
        }

        # Svaret konverteres til JSON
        response_json = json.dumps(response_data)

        connectionSocket.send(response_json.encode())
    
    # Exception i tilfælde af en manglende værdi
    except KeyError as e:
        missing_key = str(e)
        error_message = f"Missing key: '{missing_key}'. Please try again."

        response_data = {
            "error": error_message
        }
    
        response_json = json.dumps(response_data)
        connectionSocket.send(response_json.encode())



    connectionSocket.close()

# Variable
serverPort = 7

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to work for you')

while True:
    csock, addr = serverSocket.accept()
    threading.Thread(target=HandleClient, args=(csock, addr)).start()
