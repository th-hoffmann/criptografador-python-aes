
# Criptografador Python AES

Um utilitário simples de linha de comando em Python para criptografar e descriptografar arquivos usando o algoritmo AES no modo CTR.

## 🛡️ Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio de projeto da **[Formação Cybersecurity da DIO](https://web.dio.me/track/formacao-cybersecurity)**.

O desafio original propunha a implementação de um "ransomware" para fins educacionais. Esta ferramenta é uma prova de conceito que implementa a parte central dessa ideia: a **criptografia de arquivos**.

O objetivo é puramente didático, focado em demonstrar a implementação da criptografia simétrica com a biblioteca `pyaes` em Python, ajudando a entender os mecanismos por trás de malwares de criptografia para **fins de estudo e defesa**.

## ✨ Funcionalidades

  * `encripter.py`: Localiza um arquivo (`teste.txt`), criptografa seu conteúdo e o salva como `teste.txt.encripted`.
  * `decripter.py`: Localiza o arquivo `teste.txt.encripted`, descriptografa seu conteúdo usando a chave correta e o restaura.

## 💻 Tecnologias Utilizadas

  * **Python 3**
  * **`pyaes`**: Biblioteca para implementação do AES (Advanced Encryption Standard).

## 🚀 Como Usar

1.  Clone este repositório:

    ```bash
    git clone https://github.com/SEU-USUARIO/criptografador-python-aes.git
    cd criptografador-python-aes
    ```

2.  Instale a dependência necessária:

    ```bash
    pip install pyaes
    ```

3.  Crie um arquivo `teste.txt` na pasta com algum conteúdo para testar.

4.  Para **criptografar** o arquivo:

    ```bash
    python encripter.py
    ```

    *(Isso irá criar o arquivo `teste.txt.encripted` e apagar o `teste.txt` original)*

5.  Para **descriptografar** o arquivo:

    ```bash
    python decripter.py
    ```

    *(Isso irá recriar o `teste.txt` original e apagar o `teste.txt.encripted`)*

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.
