import argparse
import pysftp

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
            sftp.put(params['zip_file'])
            sftp.execute("ls -lah")
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