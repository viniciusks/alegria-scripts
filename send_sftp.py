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

    data_type = "site"

    for data in DATAS_TO_DEPLOY[data_type]:
        if "/" in data:
            if data in params["file_path"]:
                print("ENTROU NA BARRA")
                print(data)
                break
        elif not "/" in data:
            print("ENTROU NO SEM BARRA")
            print(data)
            break
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