import argparse
import pysftp

ALEGRIA_PATH_FOLDER = "/public_html/alegriacrista"
HOST_PORT = 22

pysftp.CnOpts.hostkeys = None

def main(params):
    srv = pysftp.Connection(host=params['host'], username=params['user'], password=params['pass'], port=HOST_PORT)
    srv.listdir(ALEGRIA_PATH_FOLDER)
    # with srv.cd(ALEGRIA_PATH_FOLDER):
        # srv.put(params['zip_file'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parametros para execução do dataflow stream')
    parser.add_argument('host', help='Host para realizar a conexão.')
    parser.add_argument('user', help='Usuário para realizar a conexão.')
    parser.add_argument('pass', help='Senha para realizar a conexão.')
    parser.add_argument('zip_file', help='Arquivo que deve ser transferido.')
    params = vars(parser.parse_args())

    main(params)