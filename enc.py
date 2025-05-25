from cryptography.fernet import Fernet
import os
import sys

def enc_file(key, files):
    for file_path in files:
        with open(file_path, 'rb') as bin_file:
            content = bin_file.read()
        encrypt_content = Fernet(key).encrypt(content)
        with open(file_path, 'wb') as bin_file:
            bin_file.write(encrypt_content)

def list_files(base_dir, ign_arqs):
    all_files = []
    for entry in os.listdir(base_dir):
        full_path = os.path.abspath(os.path.join(base_dir, entry))
        if os.path.isdir(full_path):
            all_files += list_files(full_path, ign_arqs)
        elif os.path.isfile(full_path) and os.path.basename(entry) not in ign_arqs:
            all_files.append(full_path)
    return all_files

def main():
    ign_arqs = [os.path.basename(__file__), 'key.key', 'enc.py', 'dec.py']
    dir = sys.argv[1] if len(sys.argv) > 1 else 'arquivos'

    if not os.path.exists(dir):
        print(f'[ERRO] Diretório "{dir}" não encontrado.')
        sys.exit(1)

    arqs = list_files(dir, ign_arqs)
    print(f'\n{len(arqs)} arquivos encontrados:\n')

    for file in arqs:
        print(file)

    if not arqs:
        print('Nenhum arquivo foi encontrado para ser encriptado.')
        return

    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    enc_file(key, arqs)
    print('\n✅ Arquivos encriptados com sucesso!')

if __name__ == '__main__':
    main()
