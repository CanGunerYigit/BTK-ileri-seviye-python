import socket 

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket metodu yardımıyla socket oluşturuyoruz
HOST=socket.gethostbyname(socket.gethostname()) #hostun yani bizim ip adresimiz
PORT=12345


server_socket.bind((HOST,PORT)) 

server_socket.listen() #bağlanacak clientları dinliyoruz

while True:
    client_socket,client_address=server_socket.accept() #bağlantı kabul ederek client socketini ve adresini alacağız
    print(f"bağlantı yapıldı: {client_address}")
    print(client_socket,client_address)
    client_socket.send("merhaba".encode("utf-8"))
    server_socket.close()
   
    break
