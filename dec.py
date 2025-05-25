from cryptography.fernet import Fernet
import os
import sys

# Constantes
DIR_DEFAULT = 'arquivos'
IGN_ARQ = [os.path.basename(__file__), 'key.key', 'enc.py', 'dec.py']
KEY_PATH = 'key.key'

def list_files(base_dir, ign_arqs):
    all_files = []
    for entry in os.listdir(base_dir):
        full_path = os.path.abspath(os.path.join(base_dir, entry))
        if os.path.isdir(full_path):
            all_files += list_files(full_path, ign_arqs)
        elif os.path.isfile(full_path) and os.path.basename(entry) not in ign_arqs:
            all_files.append(full_path)
    return all_files

def read_key(key_path):
    if not os.path.isfile(key_path):
        print(f'[ERRO] Chave de criptografia não encontrada: {key_path}')
        sys.exit(1)
    with open(key_path, 'rb') as key_file:
        return key_file.read()

def decrypt_files(key, files):
    decrypted_files = []
    for file in files:
        try:
            with open(file, 'rb') as enc_file:
                content = enc_file.read()
            raw_content = Fernet(key).decrypt(content)
            with open(file, 'wb') as dec_file:
                dec_file.write(raw_content)
            decrypted_files.append(file)
        except Exception as e:
            print(f'[ERRO] Não foi possível descriptografar "{file}": {e}')
    return decrypted_files

def print_decrypted_files(files):
    if files:
        print('\n✅ Arquivos descriptografados com sucesso:')
        for file in files:
            print(f'  - {file}')
    else:
        print('\n⚠️ Nenhum arquivo foi descriptografado.')

def main():
    dir = sys.argv[1] if len(sys.argv) > 1 else DIR_DEFAULT

    if not os.path.exists(dir):
        print(f'[ERRO] Diretório "{dir}" não encontrado.')
        sys.exit(1)

    all_files = list_files(dir, IGN_ARQ)
    key = read_key(KEY_PATH)
    decrypted_files = decrypt_files(key, all_files)
    print_decrypted_files(decrypted_files)

if __name__ == '__main__':
    main()
