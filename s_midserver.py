# -*- coding: utf-8 -*-
import socket
id = ''
pw = ''
while 1:
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP소켓 생성
    s2.bind(('', 6000))
    s2.listen(5)
    conn, addr = s2.accept()  # 클라이언트 접속
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP소켓 생성
    s.connect(('127.0.0.1', 6001))  # IP : 127.0.0.1, PORT : 6001 (서버)에 연결
    id = (conn.recv(1024)).decode()  # client로부터 받은 id, pw를 디코딩
    pw = (conn.recv(1024)).decode()
    print('아이디 : ' + id + '\n비밀번호 : ' + pw)
    s.send(id.encode())  # server로의 id, pw 전송을 위해 인코딩
    s.send(pw.encode())
    if (s.recv(1024).decode() == 'ok'):
        conn.send('ok'.encode())
    else:
        conn.send('no'.encode())  # server로부터 ok 또는 no 사인을 전송받으면 이를 client로 전달
