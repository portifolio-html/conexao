from mysql import connector

class Manipular_dados:

    def __init__(self):
        self.host = "localhost"
        self.database = "supermercado"
        self.user = "root"
        self.password = "382536"

    def conectar_basedados(self):

        conexao = connector.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
        )

        return conexao
    
    def cadastrar_dados(self, comando, dados):

        conect = self.conectar_basedados()

        with conect.cursor() as cursor:
            
            cursor.execute(comando, dados)
            conect.commit()

            print('cadastrado com sucesso!')

            conect.close()
    
    def buscar_dados(self, comando):

        conect = self.conectar_basedados()

        with conect.cursor() as cursor:
            
            cursor.execute(comando)

            dados = cursor.fetchall()

            conect.close()

            return dados

