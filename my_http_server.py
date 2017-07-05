import socket
my_socket = socket.socket()
my_socket.bind(('192.168.1.67', 1999))

# conn = 0
# conn, addr = my_socket.accept()

# print 'connected:', addr

# if (conn != 0):
#     conn.send('HTTP/1.0 200 OK \n\n')
my_socket.listen(2)
while 1:

    conn, addr = my_socket.accept()
    print 'connected:', addr
    data = conn.recv(16384)
    if not data:
        break
    conn.send(data)
    conn.close()

my_socket.close()