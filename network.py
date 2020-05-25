import socket


class Network:
    """Inicializa o cliente. Adicione o endereço ipv4 do host, LINHA 9"""

    def __init__(self):
        # Para que isso funcione na sua máquina, isso deve ser igual ao endereço ipv4 da
        # máquina que está executando o servidor
        self.host = socket.gethostbyname(socket.gethostname())
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Você pode encontrar esse endereço digitando ipconfig no CMD e copiando o endereço ipv4. Novamente,
        # esses devem ser os servidores endereço ipv4. Este campo será o mesmo para todos os seus clientes.
        self.port = 9090
        self.address = (self.host, self.port)
        self.id = self.connect()

    """Cliente se conecta ao servidor."""

    def connect(self):
        self.client.connect(self.address)
        return self.client.recv(2048).decode()

    """Envia os dados necessários para o servidor."""

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as err:
            return str(err)
