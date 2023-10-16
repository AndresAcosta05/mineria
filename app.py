from flask import Flask, render_template

from routes.mineria import mineria

SECRET_KEY = 'mykeyflask'
app = Flask(__name__)

# REGISTRAMOS LAS RUTAS
app.register_blueprint(mineria)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analisis')
def analisis():
    return render_template('analisis.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/extraccion')
def extraccion():
    return render_template('extraccion.html')

if __name__ == '__main__':
    app.run(debug=True)