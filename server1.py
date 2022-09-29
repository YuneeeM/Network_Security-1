import socket

host_ip = '127.0.0.1'
port_client = 8010
port_server2 = 8020
port_server3 = 8030

# socket 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host_ip, port_client))

# 클라이언트-서버
server_socket.listen()
print('~server1 연결 성공~')

client_socket, addr = server_socket.accept()
print('accept()')

if addr:
    print('클라이언트와 연결됨: ', addr)
else:
    print('클라이언트와 연결되지 않음')
    client_socket.close()
    server_socket.close()


# 각 서버2, 서버3으로 보내야하는 내용 전송
def expression(opn):

    data = client_socket.recv(1024)
    opn = data.decode()

   # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if '+' in opn or '-' in opn:
        client_socket.connect((host_ip, port_server2))

    elif '*' in opn or '/' in opn:
        client_socket.connect((host_ip, port_server3))

    data = opn.encode()
    client_socket.send(data)

    result = client_socket.recv(1024).decode('utf-8')
    print(result)
    return result


server_socket.close()
