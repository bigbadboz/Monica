import  sys, socket, wave

port = 3443
ip = "192.168.2.204"


#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
print ("connected to socket")

wo = wave.open("monica2.wav",'wb')
wo.setnchannels(1)
wo.setsampwidth(2)
wo.setframerate(8000)





while True:
  print ("Connection from ",  socket.gethostbyname(socket.gethostname()))
  while 1:
      data = client_socket.recv(512)
      if data:
        wo.writeframes(data)
        print ("WROTE STUFF")
        print ("RECIEVED:", data)
      else:
        break
wo.close()
client_socket.close()