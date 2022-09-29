import socket

host_ip = '127.0.0.1'

port_client = 8010
port_server2 = 8020
port_server3 = 8030


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host_ip, port_client))


server_socket.listen()
print('~~server2 연결 성공~~')

client_socket, addr = server_socket.accept()
print('accept()')


def calculate_function(opn):
    input_value = client_socket.recv(1024)
    opn = input_value.decode()

    if '+' in opn:
        result = opn.split('+')
        res_value = float(opn[0])+float(opn[1])
        res_value = str(res_value)
        client_socket.sendall(res_value.encode())

    elif '-' in opn:
        result = opn.split('-')
        res_value = float(opn[0])-float(opn[1])
        res_value = str(res_value)
        client_socket.sendall(res_value.encode())

    else:
        res_value = "계산 에러 발생!"
        res_value = str(res_value)
        client_socket.sendall(res_value.encode())
    return res_value


server_socket.close()
print("server2 종료")
