from flask import Flask, request, render_template, jsonify
from conectar_dados import *
import MySQLdb

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cad_vendas', methods=['GET', 'POST'])
def cad_vendas():

    command = Manipular_dados()

    def com():

        query = "select count(*) from cad_vendas"
        r = command.buscar_dados(query)[0][0]
        return r+1

    if request.method == 'POST':
        # Processamento dos dados
        codigo = request.form.get('codigo')
        id_nome = request.form.get('cod_cliente')
        nome = request.form.get('cliente')
        cod_produto = request.form.get('cod_produto')
        produto = request.form.get('produto')
        valor = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        total = request.form.get('total')

        query = """
            insert into cad_vendas (id_cliente, codigo_produto, quantidade) values (%s, %s, %s)
        """
        
        command.cadastrar_dados(query, (id_nome, cod_produto, quantidade))

        return render_template('cad_vendas.html', codigo=com())
    
    return render_template('cad_vendas.html', codigo=com())

@app.route('/cad_clientes', methods=['GET', 'POST'])
def cad_clientes():

    command = Manipular_dados()

    def com():

        query = "select count(*) from cad_clientes"
        r = command.buscar_dados(query)[0][0]
        return r+1

    if request.method == 'POST':

        # Processamento dos dados
        id = request.form.get('cod_cli')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')

        query = """
        insert into cad_clientes (nome, sobrenome, endereço, telefone) values (%s, %s, %s, %s)
        """

        command.cadastrar_dados(query, (nome, sobrenome, endereco, telefone))

        return render_template('cad_clientes.html', codigo=com())
    
    return render_template('cad_clientes.html', codigo=com())

@app.route('/cad_produtos', methods=['GET', 'POST'])
def cad_produtos():

    command = Manipular_dados()

    def com():

        query = "select count(*) from cad_produtos"
        r = command.buscar_dados(query)[0][0]
        return r+1

    if request.method == 'POST':

        # Processamento dos dados
        codigo = request.form.get('codigo')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')

        query = """
            insert into cad_produtos (produto, valor, quantidade) values (%s, %s, %s)
        """        
        command.cadastrar_dados(query, (descricao, preco, quantidade))

        return render_template('cad_produtos.html', codigo=com())
    
    
    
    return render_template('cad_produtos.html', codigo=com())

@app.route('/buscar_cliente', methods=['GET', 'POST'])
def buscar_cliente():

    cod_cliente = request.args.get('cod_cliente')

    command = Manipular_dados().conectar_basedados()

    if cod_cliente:
        
        try:
            cursor = command.cursor()
            query = "SELECT nome FROM cad_clientes WHERE id = %s"
            cursor.execute(query, (cod_cliente,))
            cliente = cursor.fetchone()

            if cliente:
                return jsonify({"cliente": cliente[0]})
            else:
                return jsonify({"cliente": None})
        except MySQLdb.Error as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"cliente": None}), 400

@app.route('/buscar_produto', methods=['GET', 'POST'])
def buscar_produto():

    cod_produto = request.args.get('cod_produto')

    command = Manipular_dados().conectar_basedados()

    if cod_produto:
        
        try:
            cursor = command.cursor()
            query = "SELECT produto, valor FROM cad_produtos WHERE codigo = %s"
            cursor.execute(query, (cod_produto,))
            produto = cursor.fetchone()

            if produto:
                return jsonify({"produto": produto[0], "valor": produto[1]})
            else:
                return jsonify({"produto": None, "valor": None})
        except MySQLdb.Error as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"produto": None, "valor": None}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)