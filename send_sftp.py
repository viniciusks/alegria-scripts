import argparse
import pysftp
import os
import datetime

ALEGRIA_PATH_FOLDER = "/home/storage/c/93/dd/concafras1/public_html/alegriacrista"
HOST_PORT = 22


def set_new_version(file):
    with open(file, 'r+') as file:
        lines = file.readlines()
        for line in lines:
            if "ALTERAR_VERSAO_ALEGRIA_FRONT" in line:
                date = datetime.datetime.now()
                print(f"LINHA: {line}")
                replaced_line = line.replace("ALTERAR_VERSAO_ALEGRIA_FRONT", f"{date.strftime('%d/%m/%Y, %H:%M:%S')}")
                line = replaced_line
        file.writelines(lines)
        file.close()


def main(params):
    if "index.html" in params['file_path']:
        set_new_version(params['file_path'])

    # Configurações necessárias para não verificar as chaves SSH's
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    # Início da conexão com o servidor da CONCAFRAS
    with pysftp.Connection(host=params['host'], username=params['user'], password=params['pass'], port=HOST_PORT, cnopts=cnopts, log="./log_script.log") as sftp:
        # Dentro da pasta da Alegria Cristã
        if "assets/css/pages-styles" in params['file_path']:
             print("ENTROU EM ASSETS/CSS/PAGES-STYLES")
             with sftp.cd(f"{ALEGRIA_PATH_FOLDER}/assets/css/pages-styles"):
                sftp.put(params['file_path'])
        elif "assets/css" in params['file_path']:
            print("ENTROU EM ASSETS/CSS")
            with sftp.cd(f"{ALEGRIA_PATH_FOLDER}/assets/css"):
                sftp.put(params['file_path'])
        elif "assets/img/logo" in params['file_path']:
            print("ENTROU EM ASSETS/IMG/LOGO")
            with sftp.cd(f"{ALEGRIA_PATH_FOLDER}/assets/img/logo"):
                sftp.put(params['file_path'])
        elif "assets/img" in params['file_path']:
            print("ENTROU EM ASSETS/IMG")
            with sftp.cd(f"{ALEGRIA_PATH_FOLDER}/assets/img"):
                sftp.put(params['file_path'])
        elif "assets/js" in params['file_path']:
            print("ENTROU EM ASSETS/JS")
            with sftp.cd(f"{ALEGRIA_PATH_FOLDER}/assets/js"):
                sftp.put(params['file_path'])
        elif "pages" in params['file_path']:
            print("ENTROU EM PAGES")
            with sftp.cd(f"{ALEGRIA_PATH_FOLDER}/pages"):
                sftp.put(params['file_path'])
        else:
            print("ENTROU NA RAIZ")
            with sftp.cd(f"{ALEGRIA_PATH_FOLDER}"):
                sftp.put(params['file_path'])

        # Encerrando conexão
        sftp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parametros para execução do dataflow stream')
    parser.add_argument('host', help='Host para realizar a conexão.')
    parser.add_argument('user', help='Usuário para realizar a conexão.')
    parser.add_argument('pass', help='Senha para realizar a conexão.')
    parser.add_argument('file_path', help='Arquivo que deve ser transferido.')
    params = vars(parser.parse_args())

    main(params)