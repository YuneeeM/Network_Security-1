from socket import *
import os
import sys

client_Sock = socket(AF_INET, SOCK_STREAM)
client_Sock.connect(('127.0.0.1', 8010))

print('연결 성공~...')
f_name = input('전송할 파일 이름: ')
client_Sock.sendall(f_name.encode('utf-8'))

data = client_Sock.recv(1024)
data_volumn = 0

if not data:
    print('파일 %s -> 서버에 존재하지 않음' % f_name)
    sys.exit()

now_dir = os.getcwd()
with open(now_dir+"\\"+f_name, 'wb') as f:  # 현재dir에 filename으로 파일을 받음
    try:
        while data:  # 데이터가 있을 때까지
            f.write(data)  # 1024바이트 씀
            data_volumn += len(data)
            data = client_Sock.recv(1024)  # 1024바이트를 받아 옴
    except Exception as ex:
        print(ex)
print('파일 %s 받기 완료! 전송량 %d' % (f_name, data_volumn))
