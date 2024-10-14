import socket 

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket metodu yardımıyla socket oluşturuyoruz
HOST=socket.gethostbyname(socket.gethostname()) #hostun yani bizim ip adresimiz
PORT=12345


client_socket.connect((HOST,PORT))
message=client_socket.recv(1024)
print(message.decode("utf-8"))
client_socket.close()