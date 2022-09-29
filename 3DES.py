from Crypto.Cipher import DES3
from hashlib import md5

while True:
    print('둘 중 하나를 고르시오:\n\t1.암호화\n\t2.복호화 ')
    operation = input('당신의 선택은: ')
    if operation not in ['1', '2']:
        break
    file_path = input('File path: ')
    key = input('TDES key: ')

    key_hash = md5(key.encode('ascii')).digest()

    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()

        if operation == '1':
            # 암호화
            new_file = cipher.encrypt(file_bytes)
        else:
            # 복호화
            new_file = cipher.decrypt(file_bytes)

    with open(file_path, 'wb')as output_file:
        output_file.write(new_file)
