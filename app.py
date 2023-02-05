from flask import Flask,url_for,render_template
app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hola mundo Flask '


if __name__ == '__main__':
    app.run()

@app.route('/saludar')
@app.route('/saludar/<hi>')
@app.route('/saludar/<hi>/<lang>')
def saludar(hi='andres',lang='es'):
    return 'hola :  '+hi+lang


@app.route('/html')
@app.route('/html/<name>')
def paginaweb(name="andres"):
    return '''
    <html>
        <body>
            <h1>Hola flask </h1>
            <p> Hola %s </p>

            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </lu>
        </body>
    </html>        
    
    ''' %name
@app.route('/static_file')
def static_file():
    #return"<imag src='"+url_for('static',filename='img/flask2.png')+"'>" 
    return "<img src='/static/img/flask2.png' > "


@app.route('/template')
@app.route('/template/<name>')
def template(name="andres"):
    return render_template('view.html',name=name)


if __name__ == '__main__':
    app.run()

 
