from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Brayan!"

@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    usuario = request.form['usuario']
    senha = request.form['password']
    print "usuario " + usuario
    if usuario == 'techa' and senha == 'vaga':
      session['estalogado'] = True

    return redirect("/pagina")

  session['estalogado'] = False
  return render_template("login.html")

@app.route("/pagina", methods=['GET', 'POST'])
def pagina():
  if request.method == 'GET':
    if session['estalogado']:
      return render_template("index.html")
    else:
      session['estalogado'] = False
      return redirect("/login")
  else:
    session['estalogado'] = False
    return redirect("/login")

if __name__ == "__main__":
  app.secret_key = 'sadkljfsdakljfsdajklfsdlajkklsdjaklhweioyweq34'
  app.session_type = 'memcache'
  app.debug = True
  app.run(host='0.0.0.0', port=8078)
