# 🛡️ Ransomware Educacional em Python (Uso Responsável)

⚠️ **Aviso Legal:** Este código tem fins **exclusivamente educacionais** para aprendizado sobre criptografia e segurança. **O uso deste software para prejudicar terceiros é ilegal e antiético. Use apenas em seus próprios arquivos e em ambientes controlados.**

## 📄 Descrição

Este projeto consiste em dois scripts Python que simulam o funcionamento básico de um ransomware:

- **enc.py**: encripta arquivos em um diretório usando criptografia simétrica (Fernet).
- **dec.py**: descriptografa os arquivos usando a chave gerada no processo de encriptação.

O objetivo é demonstrar conceitos de criptografia e manipulação de arquivos em Python.

## 🧠 Como Funciona

- O script de encriptação (`enc.py`) percorre recursivamente um diretório, ignora arquivos específicos (ex: o próprio script, a chave e scripts de decodificação) e encripta os arquivos restantes usando uma chave Fernet.
- A chave gerada é salva em um arquivo `key.key`.
- O script de decriptação (`dec.py`) usa a chave em `key.key` para descriptografar os arquivos previamente criptografados.
- Arquivos que não podem ser descriptografados geram mensagens de erro, mas o processo continua para os demais.

## 🔧 Requisitos

- Python 3 instalado
- Biblioteca `cryptography`

Para instalar a biblioteca necessária, use:

```bash
pip install cryptography
```

## 🚀 Como Usar

### Encriptar arquivos

1. Coloque os arquivos que deseja encriptar dentro da pasta `arquivos` (ou especifique outro diretório ao executar).
2. Execute:

```bash
python enc.py [diretório]
```

Exemplo, para a pasta padrão `arquivos`:

```bash
python enc.py
```

Será criado o arquivo `key.key` com a chave de criptografia.

### Descriptografar arquivos

1. Certifique-se de que o arquivo `key.key` está presente no diretório do script.
2. Execute:

```bash
python dec.py [diretório]
```

Exemplo, para a pasta padrão `arquivos`:

```bash
python dec.py
```

Os arquivos criptografados serão descriptografados.

## ⚠️ Aviso Importante

Este projeto é apenas para fins educativos e experimentais! **Não utilize este código para fins maliciosos.** A responsabilidade pelo uso é inteiramente do usuário.
