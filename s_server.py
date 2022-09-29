from socket import *
from os.path import exists
import sys

server_Sock = socket(AF_INET, SOCK_STREAM)
server_Sock.bind(('', 8010))
server_Sock.listen(1)

connect_Sock, addr = server_Sock.accept()

print(str(addr), 'connect!')

# Client한테 file name(Binary ByteStream 형태)을 전달 받음
f_name = connect_Sock.recv(1024)
print('receive data : ', f_name.decode('utf-8'))  # filename을 일반 문자열로 변환
data_volumn = 0

if not exists(f_name):
    print("no-----file")
    sys.exit()

print("file %s 전송 시작!" % f_name)
with open(f_name, 'rb') as f:
    try:
        data = f.read(1024)  # 1024바이트 읽음
        while data:  # 데이터가 없을 때까지
            data_volumn += connect_Sock.send(data)  # 1024바이트 보내고 크기 저장
            data = f.read(1024)  # 1024바이트 읽음
    except Exception as excep:
        print(excep)
print("전송완료 %s, 전송량 %d" % (f_name, data_volumn))
