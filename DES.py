from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)


def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


nonce, ciphertext, tag = encrypt(input('암호화할 문장을 입력하세요: '))
plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher-text: {ciphertext}')

if not plaintext:
    print('error: 메시지가 손상되었습니다!')
else:
    print(f'Plain-text: {plaintext}')
