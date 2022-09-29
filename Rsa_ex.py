from inspect import signature
from pydoc import plain
import rsa


def generate_keys():
    (pubKey, privKey) = rsa.newkeys(1024)
    with open('keys/pubKey.pem', 'wb') as f:
        f.write(pubKey.save_pkcsl('PEM'))
    with open('Keys/privKey.pem', 'wb') as f:
        f.write(privKey.save_pkcsl('PEM'))


def load_keys():
    with open('Keys/pubKey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())
    with open('Keys/privKey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey


def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


def sign_shal(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')


def verify_shal(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False


generate_keys()
pubKey, privKey = load_keys()

message = input('Enter a message: ')
ciphertext = encrypt(message, pubKey)

signature = sign_shal(message, privKey)
plaintext = decrypt(ciphertext, privKey)

print('Cipher text: {ciphertext}')
print('Signature: {signature}')

if plaintext:
    print('Plain text: {plainrext}')
else:
    print('Could not decrypt the message.')

if verify_shal(plaintext, signature, pubKey):
    print('Signature verified!')
else:
    print('Could not verify the message signature.')
