from flask import Flask, request, render_template, flash
from mysql import connector
from mysql.connector import Error

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


class Cadastrar_dados:

    def __init__(self, comando):
        self.host = "localhost"
        self.database = "supermercado"
        self.user = "root"
        self.password = "382536"

        self.comando = comando

    def conectar_basedados(self):

        conexao = connector.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
        )

        with conexao.cursor() as cursor:
            
            cursor.execute(self.comando)
            conexao.commit()

            print('cadastrado com sucesso!')

            conexao.close()




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cad_vendas', methods=['GET', 'POST'])
def cad_vendas():

    if request.method == 'POST':
        # Processamento dos dados
        codigo = request.form.get('codigo')
        nome = request.form.get('cliente')
        cod_produto = request.form.get('cod_produto')
        produto = request.form.get('produto')
        valor = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        total = request.form.get('total')

        dados = (codigo, nome, cod_produto, quantidade)

        Cadastrar_dados("cad_vendas", dados).conectar_basedados()

        return render_template('index.html')
    
    return render_template('cad_vendas.html')

@app.route('/cad_clientes', methods=['GET', 'POST'])
def cad_clientes():
    if request.method == 'POST':
        # Processamento dos dados
        id = request.form.get('cod_cli')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')

        query = f"insert into cad_clientes (nome, sobrenome, endereço, telefone) values ({nome}, {sobrenome}, {endereco}, {telefone})"

        Cadastrar_dados(query).conectar_basedados()

        return render_template('index.html')
    
    return render_template('cad_clientes.html')

@app.route('/cad_produtos', methods=['GET', 'POST'])
def cad_produtos():
    if request.method == 'POST':
        # Processamento dos dados
        codigo = request.form.get('codigo')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')

        print(codigo, descricao, preco, quantidade)

        return render_template('index.html')
    return render_template('cad_produtos.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)