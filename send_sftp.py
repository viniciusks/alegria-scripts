import argparse
import pysftp
import os

ALEGRIA_PATH_FOLDER = "/home/storage/c/93/dd/concafras1/public_html/alegriacrista"
HOST_PORT = 22

def unzip_file(zip_file):
    os.system("pwd")
    os.system("mkdir dist")
    os.system(f"unzip {zip_file} dist/")
    os.system("ls -lah")
    dirlist = os.listdir("dist/")
    files = []
    for i in dirlist:
        files.append(os.path.abspath(i))
    return files


def main(params):
    files = unzip_file(params['zip_file'])
    print(files)
    # Configurações necessárias para não verificar as chaves SSH's
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    # Início da conexão com o servidor da CONCAFRAS
    with pysftp.Connection(host=params['host'], username=params['user'], password=params['pass'], port=HOST_PORT, cnopts=cnopts, log="./log_script.log") as sftp:
        # Dentro da pasta da Alegria Cristã
        with sftp.cd(ALEGRIA_PATH_FOLDER):
            sftp.put(params['zip_file'])
            print(sftp.listdir())
            # sftp.execute("ls -lah")
        # Encerrando conexão
        sftp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parametros para execução do dataflow stream')
    parser.add_argument('host', help='Host para realizar a conexão.')
    parser.add_argument('user', help='Usuário para realizar a conexão.')
    parser.add_argument('pass', help='Senha para realizar a conexão.')
    parser.add_argument('zip_file', help='Arquivo que deve ser transferido.')
    params = vars(parser.parse_args())

    main(params)