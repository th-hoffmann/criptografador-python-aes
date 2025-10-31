import os
import pyaes

## Abrir o arquivo a ser descriptografado

file_name = 'teste.txt.encripted'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Definir a chave de descriptografia

key = b"ramsowareteste12"
aes = pyaes.AESModeOfOperationCTR(key)

## Descriptografar os dados
decrypted_data = aes.decrypt(file_data)

## Salvar os dados descriptografados em um novo arquivo
new_file = file_name.replace('.encripted', '')
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted_data)
new_file.close()
