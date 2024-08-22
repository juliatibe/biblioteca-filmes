from flask import Flask, render_template, request, redirect
app = Flask(__name__)

nn_filme[]
diretor[]


@app.route('/')
def index():
    return render_template ('index.html', diretor=diretor, nn_filmes=nn_filmes)

@app.route('/verificar_filmes', methods=['GET', 'POST'])
def verificar_filmes():
    if request.method == 'POST':
        nn_filme = request.form['nn_filme']
        diretor = request.form['diretor']
        genero_filme = request.form['genero_filme']
        armazenamento = len(nn_filme)
        nn_filme.append([armazenamento, nn_filme, diretor, genero_filme])
        return redirect('/biblioteca.html')

 @app.route('/editar_filme', methods= ['GET', 'POST'])
 def editar_filmes():