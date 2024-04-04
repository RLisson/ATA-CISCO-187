from ftplib import FTP
import os


def replace_words(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


FTP_SERVER = 'SERVER'
FTP_USER = 'USER'
FTP_PASS = 'PASS'
FTP_PORT = 21

SIP_SERVER = input("Insira o servidor: ")
SIP_USER = input("Insira o usuário: ")
SIP_PASS = input("Insira a senha: ")
ATA_MAC = input("Insira o MAC do ATA: ")
while len(ATA_MAC) != 12:
    print("MAC inválido")
    ATA_MAC = input("Insira o MAC do ATA: ")

LINE = int(input("Você deseja configurar line 1 ou 2: "))
while LINE != 1 and LINE != 2:
    print("Valor inválido, insira apenas 1 ou 2")
    LINE = int(input("Você deseja configurar line 1 ou 2: "))

if LINE == 2:
    ATA_MAC = ATA_MAC[2:] + '01'
FILE_NAME = 'ATA' + ATA_MAC + '.cnf.xml'

with open('ATA', 'r') as file:
    filedata = file.read()

replace = {
    'SERVER': SIP_SERVER,
    'LINE': SIP_USER,
    'PASSWORD': SIP_PASS
}

filedata = replace_words(filedata, replace)

with open(FILE_NAME, 'w') as file:
    file.write(filedata)

session = FTP()
session.connect(FTP_SERVER, FTP_PORT)
session.login(FTP_USER, FTP_PASS)

file = open(FILE_NAME, 'rb')
session.storbinary(f'STOR {FILE_NAME}', file)
file.close()
session.quit()

os.remove(FILE_NAME)
