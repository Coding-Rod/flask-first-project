from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template('home.html', title='Restaurante de comida rápida')

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    if request.method == 'GET':
        return render_template('form.html', title='Pedido')
    if request.method == 'POST':
        print(request.form)
        with open('data/db.json', 'r') as file:
            data = json.load(file)
            data.append(request.form)
        with open('data/db.json', 'w') as file:
            json.dump(data, file, indent=4)
        flash('Datos enviados correctamente')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)