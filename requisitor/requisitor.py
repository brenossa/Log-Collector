import requests

class LogRequisitor:
    def __init__(self, host, port, endpoint="criar_post"):
        self.host = host
        self.port = port
        self.endpoint = endpoint
        self.api_url = f"http://{host}:{port}/{endpoint}"

    def criar_novo_post(self, titulo, conteudo, autor):
        data = {
            'titulo': titulo,
            'conteudo': conteudo,
            'autor': autor
        }
        response = requests.post(self.api_url, data=data)
        return response.status_code == 200
