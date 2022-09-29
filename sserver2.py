import socket

IP_1 = '127.0.0.1'
PORT1 = 8020


try:
    # TCP 소켓 생성 / 서버 1 연결
    server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2.bind((IP_1, PORT1))
    server2.listen()
    print('~~server2 연결성공~~')

    server2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server1, addr = server2.accept()

    print("연결 :", addr)

    while True:
        num_value = []
        result = 0

        recvData = server1.recv(1024)
        recvData = recvData.decode()

        print("메인서버-> 계산식", addr, ':',  recvData)

        if ("exit" in recvData) or "" == recvData:
            print("~~서버2 종료~~")
            break

        if '*' in recvData:
            num_value = recvData.split('*')
            result = float(num_value[0]) * float(num_value[1])
            result = str(result)
            server1.sendall(result.encode('utf-8'))

        elif '/' in recvData:
            num_value = recvData.split('/')
            result = float(num_value[0]) / float(num_value[1])
            result = str(result)
            server1.sendall(result.encode('utf-8'))


except:
    server1.close()
    server2.close()

server1.close()
server2.close()
