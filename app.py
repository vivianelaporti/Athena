from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    context = {
        'title': 'Athena',
        'login': True
    }
    return render_template('pagLogin.html', context=context)

@app.route('/index')
def index():
    context = {
        'title': 'Athena',
        'index': True,
        'lista': ['nome1', 'nome2', 'nome3', 'nome4', 'nome final']
    }
    return render_template('index.html', context=context)


@app.route('/lstHistorias')
def lstHistorias():
    context = {
        'title': 'Athena',
        'lstHistorias': True,
        'lista': ['nome1', 'nome2', 'nome3', 'nome4', 'nome final']
    }
    return render_template( 'lstHistorias.html', context=context)


@app.route('/cadastrohistoriaspac')
def cadastrohistoriaspac():
    context = {
        'title': 'Athena',
        'cadastrohistoriaspac': True,
     }
    return render_template( 'pagCadHistoriaPac.html', context=context)


@app.route('/cadusuario')
def cadusuario():
    context = {
        'title': 'Athena - Cadasatro de Usuários',
        'cadusuario': True
    }
    return render_template('cadUsuario.html', context=context)



@app.route('/participante')
def participante():
    context = {
        'title': 'Athena',
        'participante': True
    }
    return render_template('pagParticipante.html', context=context)

@app.route('/medicamento')
def medicamento():
    context = {
        'title': 'Athena',
        'medicamento': True
    }
    return render_template('medicamentos.html', context=context)



@app.route('/ExercTer')
def ExercTer():
    context = {
        'title': 'Athena',
        'ExercTer': True
    }
    return render_template('EXERCtERAPEUTICO.HTML', context=context)

@app.route('/lstParticipantes')
def lstParticipantes():
    context = {
        'title': 'Athena',
        'lstParticipantes': True,
        'listap': ['nomep1', 'nomep2', 'nomep3', 'nomep4', 'nomep final']
    }
    return render_template( 'lstParticipantes.html', context=context)



if __name__ == '__main__':
    app.run(debug=True)
