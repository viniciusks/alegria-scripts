import argparse
import pysftp

ALEGRIA_PATH_FOLDER = "/home/storage/c/93/dd/concafras1/public_html/alegriacrista"
HOST_PORT = 22
DATAS_TO_DEPLOY = {
    "site": [
        "/assets/css/pages-styles",
        "/assets/css",
        "/assets/img/logo",
        "/assets/img",
        "/assets/js",
        "/pages",
        "favicon.ico",
        "index.html"
    ],
    "audio-player": [
        "index.html"
    ]
}

def main(params):
    # Configurações necessárias para não verificar as chaves SSH's
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    data_type = params["type"]

    # Início da conexão com o servidor da CONCAFRAS
    with pysftp.Connection(host=params['host'], username=params['user'], password=params['pass'], port=HOST_PORT, cnopts=cnopts, log="./log_script.log") as sftp:
        # Dentro da pasta da Alegria Cristã
        for data in DATAS_TO_DEPLOY[data_type]:
            if data in params["file_path"]:
                if "/" in data:
                    print("ENTROU NA BARRA")
                    print(data)
                    with sftp.cd(f"{ALEGRIA_PATH_FOLDER}{data}"):
                        sftp.put(params['file_path'])
                    break
                elif not "/" in data:
                    print("ENTROU NO SEM BARRA")
                    print(data)
                    with sftp.cd(f"{ALEGRIA_PATH_FOLDER}"):
                        sftp.put(params['file_path'])
                    break
        # Encerrando conexão
        sftp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parametros para execução do dataflow stream')
    parser.add_argument('host', help='Host para realizar a conexão.')
    parser.add_argument('user', help='Usuário para realizar a conexão.')
    parser.add_argument('pass', help='Senha para realizar a conexão.')
    parser.add_argument('file_path', help='Arquivo que deve ser transferido.')
    parser.add_argument('type', help='Tipo da aplicação.')
    params = vars(parser.parse_args())

    main(params)