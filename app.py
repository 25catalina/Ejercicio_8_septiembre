from flask import Flask, render_template, request, redirect

app = Flask(__name__) 

@app.route("/", methods = ["GET","POST"]) #formulario de registro
def registro():
    return render_template("index.html")


@app.route("/lista") #la tabla del diablo
def tabla():
    return render_template("lista.html")


@app.route("/procesar_registro", methods=["POST"])
def formulario ():
    datos = {"nombre": request.form['nombre'],
                      "apellido": request.form['apellido'],
                      "edad": request.form['edad']}
    return redirect ("/lista")

if __name__ == "__main__":

    app.run(debug=True)
