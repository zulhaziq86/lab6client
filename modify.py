import socket

ClientSocket = socket.socket()
host = '192.168.0.161'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))

Response = ClientSocket.recv(1024).decode()
print(Response)

while True:
    print (' L - Logarithmic \n S - Square Root \n E - Exponential \n Q - Quit')
    Input = input('\nChoose a mathematical function : ')
    
    if Input == 'L' :
        option = "log"
        value = input('Value : ')
        base = input('Base : ')
        l = option + '.' + value + '.' + base
        ClientSocket.send(str.encode(l))
    elif Input == 'S':
        option = "sq"
        value = input('Value : ')
        value2 = "0"
        s = option + '.' + value + "." + value2
        ClientSocket.send(str.encode(s))
    elif Input == 'E':
        option = "exp"
        value = input('Value : ')
        value2 = "0"
        e = option + '.' + value + "." + value2
        ClientSocket.send(str.encode(e))
    elif Input == "Q":
        option = "qt"
        ClientSocket.send(str.encode(option))
        print ('Goodbye!! \n')
        ClientSocket.close()
    else :
        print ('Invalid funtion! Try Again \n')
        
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()
