from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'amora123'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/funcionarios', methods=['GET', 'POST'])
@login_required
def funcionarios():
    funcionario_sql = select(Funcionario)
    funcionario_resultado = db_session.execute(funcionario_sql).scalar().all()
    return render_template('funcionarios.html', lista_funcionarios=funcionario_resultado)


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")
@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            flash("Preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/subtracao', methods=['GET', 'POST'])
def subtracao():
    if request.method == 'POST':
        if request.form['form-n3'] and request.form['form-n4']:
            n3 = int(request.form['form-n3'])
            n4 = int(request.form['form-n4'])
            subtracao = n3 - n4
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n3=n3, n4=n4, subtracao=subtracao)
        else:
            flash("Preencha o campo para realizar a subtração", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n5'] and request.form['form-n6']:
            n5 = int(request.form['form-n5'])
            n6 = int(request.form['form-n6'])
            multiplicar = n5 * n6
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n5=n5, n6=n6, multiplicar=multiplicar)
        else:
            flash("Preencha o campo para realizar a multiplicação", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n7'] and request.form['form-n8']:
            n7 = int(request.form['form-n7'])
            n8 = int(request.form['form-n8'])
            dividir = n7 / n8
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n7=n7, n8=n8, dividir=dividir)
        else:
            flash("Preencha o campo para realizar a divisão", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/triangulo_perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            n2 = 3
            triangulo_perimetro = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=3, triangulo_perimetro=triangulo_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/triangulo_area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3= 2
            triangulo_area = n1 * n2 / n3
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, n3=2, triangulo_area=triangulo_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/circulo_perimetro', methods=['GET', 'POST'])
def circulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n9']:
            n7 = 2
            n8 = 3.14
            n9= int(request.form['form-n9'])
            circulo_perimetro = n7 * n8 * n9
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n7=2, n8=3.14, n9=n9, circulo_perimetro=circulo_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/circulo_area', methods=['GET', 'POST'])
def circulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1= int(request.form['form-n1'])
            circulo_area = 3.14 * n1 * n1
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, circulo_area=circulo_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/quadrado_perimetro', methods=['GET', 'POST'])
def quadrado_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            n2 = 4
            quadrado_perimetro = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=4, quadrado_perimetro=quadrado_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")
@app.route('/quadrado_area', methods=['GET', 'POST'])
def quadrado_area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            quadrado_area = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, quadrado_area=quadrado_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/hexagono_perimetro', methods=['GET', 'POST'])
def hexagono_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            n2 = 6
            hexagono_perimetro = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=6, hexagono_perimetro=hexagono_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/hexagono_area', methods=['GET', 'POST'])
def hexagono_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            n2 = 6
            n4 = 4
            n3 = 1.7
            hexagono_area = n2 * n1 * n1 * n3 / n4
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=6, n3=1.7, n4=4, hexagono_area=hexagono_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        if email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                # se encontrado na base de dados
                if resultado_email.check_password(senha):
                    # login correto
                    login_user(resultado_email)
                    flash(f'Logado com sucesso', 'success')
                    return redirect(url_for('home'))
                else:
                    # login incorreto
                    flash('Senha incorreta', 'danger')
                    return render_template('login.html')
            else:
                # se não encontrado
                flash(f'Email nao encontrado', 'danger')
                return render_template('login.html')
        else:
            flash('Preencha todos os campos', 'danger')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logout com sucesso', 'success')
    return redirect(url_for('login'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        data_nascimento = request.form.get('form-data_nascimento')
        cpf = request.form.get('form-cpf')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = request.form.get('form-salario')
        ver_email = select(Funcionario).where(Funcionario.email == email)
        exists_email = db_session.execute(ver_email).scalar_one_or_none()
        if exists_email:
            flash(f'Email {email} ja esta cadastrado', 'danger')
            return render_template('cadastro.html')
        try:
            novo_func = Funcionario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, email=email, cargo=cargo, salario=salario)
            novo_func.set_password(senha)
            db_session.add(novo_func)
            db_session.commit()
            flash(f'Funcionario {nome} cadastrado com sucesso', 'success')
            return redirect(url_for('cadastro_funcionario'))
        except Exception as e:
            flash(f'Erro na base de dados ao cadastrar usuario: {e}', 'danger')
            print(f'Erro na base de dados:{e}')
            db_session.rollback()
    return render_template('cadastro.html')

@app.route('/animais')
def animais():
    return  render_template('animais.html')

#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True, port=5005)