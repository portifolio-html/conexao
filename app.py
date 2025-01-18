from flask import Flask, request, render_template, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

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

        print(codigo, nome, cod_produto, produto, valor, quantidade, total)

        flash('Login realizado com sucesso!', 'success')
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

        print(id, nome, sobrenome, endereco, telefone)

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
    app.run(debug=True)