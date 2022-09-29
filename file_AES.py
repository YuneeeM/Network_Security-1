
import hashlib
import os
from Crypto.Cipher import AES
from Crypto import Random


def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "(enc)"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' '*(16-(len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[11:]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decrypt = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decrypt.decrypt(chunk))

            outfile.truncate(filesize)


def getKey(password):
    hasher = sha256.new(password.encode('utf-8'))
    return hasher.digest()


def Main():
    choice = input("암호화,복호화 하시겠습니까? E/D 선택해주세요! ")

    if choice == 'E':
        filename = input("File: ")
        password = input("Password: ")
        encrypt(getKey(password), filename)
        print('성공')
    elif choice == 'D':
        filename = input("File: ")
        password = input("Password: ")
        decrypt(getKey(password), filename)
        print("성공")

    else:
        print("선택하지 않았기에 종료합니다.")


Main()
