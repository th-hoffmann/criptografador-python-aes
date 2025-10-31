# Criptografador Python AES 🔐

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Um utilitário de linha de comando em Python para criptografar e descriptografar arquivos usando o algoritmo AES (Advanced Encryption Standard) no modo CTR.

## 🛡️ Sobre o Projeto

Este projeto foi desenvolvido como parte do desafio de projeto da **[Formação Cybersecurity da DIO](https://web.dio.me/track/formacao-cybersecurity)** 🎓

O desafio original propunha a implementação de um "ransomware" para fins educacionais. Esta ferramenta é uma prova de conceito que implementa a parte central dessa ideia: a **criptografia de arquivos**.

> ⚠️ **Aviso**: Este projeto tem finalidade exclusivamente educacional, focado em demonstrar a implementação da criptografia simétrica para fins de estudo e defesa.

## ✨ Funcionalidades

- 🔒 **Criptografia** (`encrypter.py`):
  - Localiza o arquivo `teste.txt`
  - Criptografa seu conteúdo usando AES-CTR
  - Salva como `teste.txt.encrypted`

- 🔓 **Descriptografia** (`decrypter.py`):
  - Localiza o arquivo `teste.txt.encrypted`
  - Descriptografa usando a chave correta
  - Restaura o arquivo original

## 💻 Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
- **`pyaes`**: Implementação pura do AES em Python

## 🚀 Como Usar

### Preparação do Ambiente

1. Clone este repositório:
    ```bash
    git clone https://github.com/SEU-USUARIO/criptografador-python-aes.git
    cd criptografador-python-aes
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    
    # No Linux/macOS
    source venv/bin/activate
    
    # No Windows
    venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Uso

1. Para **criptografar**:
    ```bash
    python scripts/encrypter.py
    ```

2. Para **descriptografar**:
    ```bash
    python scripts/decrypter.py
    ```

## 📋 Requisitos

- Python 3.8 ou superior
- pyaes

## 👏 Agradecimentos

- [Digital Innovation One](https://dio.me/) pela proposta do projeto
- Comunidade Python pelos recursos e ferramentas

---

<p align="center">
  Desenvolvido com ❤️ para fins educacionais
</p>
