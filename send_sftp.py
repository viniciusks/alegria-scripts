import argparse
import pysftp
import os

ALEGRIA_PATH_FOLDER = "/home/storage/c/93/dd/concafras1/public_html/alegriacrista"
HOST_PORT = 22

def main(params):
    # Configurações necessárias para não verificar as chaves SSH's
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    # Início da conexão com o servidor da CONCAFRAS
    with pysftp.Connection(host=params['host'], username=params['user'], password=params['pass'], port=HOST_PORT, cnopts=cnopts, log="./log_script.log") as sftp:
        # Dentro da pasta da Alegria Cristã
        with sftp.cd(ALEGRIA_PATH_FOLDER):
            if("assets" in params['file_path']):
                with sftp.cd("assets"):
                    if("css" in params['file_path']):
                        if("page-styles" in params['file_path']):
                            sftp.put(params['file_path'])
                        sftp.put(params['file_path'])
            sftp.put(params['file_path'])
            print(sftp.listdir())
            # sftp.execute("ls -lah")
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