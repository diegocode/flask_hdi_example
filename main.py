from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/ayuda')
def dar_ayuda():
    return render_template('ayuda.html')


@app.route('/cantidad')
def devuelve_cantidad():
    cn = sqlite3.connect('datos.db')
    resu = cn.execute("SELECT * FROM DATOSHDI;")
    cant = len(resu.fetchall())
    cn.close()
    return render_template('cantidad.html',
                          subtitulo='',
                          cant_paises=cant)


@app.route('/cantidad_alta')
def devuelve_cantidad_alta():
    cn = sqlite3.connect('datos.db')
    resu = cn.execute("SELECT * FROM DATOSHDI WHERE HDI > 0.8;")
    cant = len(resu.fetchall())
    cn.close()
    return render_template('cantidad.html',
                          subtitulo='con HDI > 0.8',
                          cant_paises=cant)


@app.route('/listado')
def lista_top10():
    cn = sqlite3.connect('datos.db')
    q = """SELECT *
               FROM
                   DATOSHDI
               WHERE
                   HDI > 0.8
               ORDER BY
                   HDI DESC
               LIMIT 10;
        """
    resu = cn.execute(q)
    nueva_lista = resu.fetchall()
    cn.close()
    return render_template('lista.html',
                         lista=nueva_lista
                        )


@app.route('/contacto')
def contacto():
      return render_template('contacto.html')


app.run(host='0.0.0.0', port=8081, debug=True)
