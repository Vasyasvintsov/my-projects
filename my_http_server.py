import socket
my_socket = socket.socket()
my_socket.bind(('192.168.0.33', 1966))
my_socket.listen(1)
# conn = 0
conn, addr = my_socket.accept()

print 'connected:', addr

# if (conn != 0):
#     conn.send('HTTP/1.0 200 OK \n\n')

while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)

conn.close()