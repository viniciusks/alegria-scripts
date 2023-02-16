import argparse
import pysftp

ALEGRIA_PATH_FOLDER = "/home/storage/c/93/dd/concafras1/public_html/alegriacrista/"
HOST_PORT = 22
FOLDERS_TO_DEPLOY = [
    "assets/css/pages-styles",
    "assets/css",
    "assets/img/logo",
    "assets/img",
    "assets/js",
    "pages",
    "index.html"
]
FILES = [
    "index.html"
]


def main(params):
    # Configurações necessárias para não verificar as chaves SSH's
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    # Início da conexão com o servidor da CONCAFRAS
    with pysftp.Connection(host=params['host'], username=params['user'], password=params['pass'], port=HOST_PORT, cnopts=cnopts, log="./log_script.log") as sftp:
        for folder in FOLDERS_TO_DEPLOY:
            path = f"{ALEGRIA_PATH_FOLDER}{folder}"
            # Dentro da pasta da Alegria Cristã
            if folder in params['file_path']:
                if folder in FILES:
                    print("ENTROU NA RAIZ")
                    with sftp.cd(f"{ALEGRIA_PATH_FOLDER}"):
                        sftp.put(params['file_path'])
                else:
                    print(f"ENTROU EM {path.upper()}")
                    with sftp.cd(f"{path}"):
                        sftp.put(params['file_path'])
            else:
                print("Não faz nada.")

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