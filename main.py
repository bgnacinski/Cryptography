# int({value}, 2) conversts (bin) -> (dec)
# int({value}, 16) converts (hex) -> (bin)
# int({value}, 8) converts (oct) -> (dec)

from os import system as sys_command
import time

class Encrypter():
    def __init__(self, word, **kwargs):
        self.word_to_encrypt = list(word)

    def ascii_encryption(self):
        output = ""

        for i in range(0, len(self.word_to_encrypt)):
            data = ord(self.word_to_encrypt[i])
            output += str(data) + " "

        return output

    def binary_encryption(self):
        output = ""

        for i in range(0, len(self.word_to_encrypt)):
            data = ord(str(self.word_to_encrypt[i]))

            output += str(bin(data)[2:]) + " "

        return output

    def hex_encryption(self):
        output = ""

        data_to_encrypt = self.binary_encryption().split()

        for i in range(0, len(self.word_to_encrypt)):
            data = hex(int(data_to_encrypt[i]))

            output += str(data).replace("0x", "") + " "

        return output

    def octal_encryption(self):
        output = ""

        data_to_encrypt = self.binary_encryption().split()

        for i in range(0, len(data_to_encrypt)):
            data = oct(int(data_to_encrypt[i]))

            output += data.replace("0o", "") + " "

        return output

class Decrypter():
    def __init__(self, encrypted_msg, **kwargs):
        self.msg_to_decrypt = encrypted_msg.split()

    def ascii_decryption(self):
        output = ""

        for i in range(0, len(self.msg_to_decrypt)):
            data = chr(int(self.msg_to_decrypt[i]))

            output += data

        return output

    def binary_decryption(self):
        output = ""

        for i in range(0, len(self.msg_to_decrypt)):
            data = int(self.msg_to_decrypt[i], 2)

            output += chr(data)

        return output

    def hex_decryption(self):
        output = ""

        data_to_decrypt = self.msg_to_decrypt

        for i in range(0, len(data_to_decrypt)):
            data = int(data_to_decrypt[i], 16)

            output += chr(int(str(data), 2))

        return output

    def octal_decryption(self):
        output = ""

        data_to_decrypt = self.msg_to_decrypt

        for i in range(0, len(data_to_decrypt)):
            data = int(data_to_decrypt[i], 8)

            output += chr(int(str(data), 2))

        return output

while True:
    sys_command("cls")

    print("Choose one of following options:")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("[?] --> "))

    if choice == 1:
        sys_command("cls")
        
        print("Message:")
        msg = input("[?] --> ")

        print("Encoding:")
        encoding = input("[?] --> ")

        if encoding == "octal":
            enc = Encrypter(msg)
            print(enc.octal_encryption())

            f = open("msg.enc", "w")
            f.write(enc.octal_encryption())
            f.close()

            time.sleep(5)

        elif encoding == "hex":
            enc = Encrypter(msg)
            print(enc.hex_encryption())

            f = open("msg.enc", "w")
            f.write(enc.hex_encryption())
            f.close()

            time.sleep(5)

        elif encoding == "ascii":
            enc = Encrypter(msg)
            print(enc.ascii_encryption())

            f = open("msg.enc", "w")
            f.write(enc.ascii_encryption())
            f.close()

            time.sleep(5)

        elif encoding == "binary":
            enc = Encrypter(msg)
            enc.binary_encryption()

            f = open("msg.enc", "w")
            f.write(enc.binary_encryption())
            f.close()

            time.sleep(5)


    elif choice == 2:
        sys_command("cls")
        
        print("Message:")
        msg = input("[?] --> ")

        print("Encoding:")
        encoding = input("[?] --> ")

        if encoding == "octal":
            dec = Decrypter(msg)
            print(dec.octal_decryption())

            f = open("decrypted_msg.txt", "w")
            f.write(dec.octal_decryption())
            f.close()

            time.sleep(5)

        elif encoding == "hex":
            dec = Decrypter(msg)
            print(dec.hex_decryption())

            f = open("decrypted_msg.txt", "w")
            f.write(dec.hex_decryption())
            f.close()

            time.sleep(5)

        elif encoding == "ascii":
            dec = Decrypter(msg)
            print(dec.ascii_decryption())

            f = open("decrypted_msg.txt", "w")
            f.write(dec.ascii_decryption())
            f.close()

            time.sleep(5)

        elif encoding == "binary":
            dec = Decrypter(msg)
            print(dec.binary_decryption())
            
            f = open("decrypted_msg.txt", "w")
            f.write(dec.binary_decryption())
            f.close()

            time.sleep(5)

    else:
        sys_command("cls")
        print("Try:")
        print(" 1 to encrypt")
        print(" 2 to decrypt")

        time.sleep(2)