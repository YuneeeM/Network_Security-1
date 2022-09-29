import socket

host_ip = '127.0.0.1'

port_client = 8010
port_server2 = 8020
port_server3 = 80305+2
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host_ip, port_client))

if client_socket:
    print("서버와 연결 성공")
    print("~~~~계산시작~~~~")
    print("'exit'입력 시 계산종료 가능")
    while True:
        calculate_num = input("수식을 입력하세요: ")
        calculate_num = calculate_num.lower()
        if 'exit' in calculate_num:
            client_socket.sendall(calculate_num.encode())
            break
        client_socket.sendall(calculate_num.encode())
        data_value = client_socket.recv(1024)
        result = data_value.decode()
        print('결과값: ', repr(result))

else:
    print('~~server와 연결하지 못하였습니다~~')
    print('계산 프로그램을 종료합니다!')

client_socket.close()
