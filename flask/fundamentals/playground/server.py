from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/<path:path>')
def catch_all(path):
    return 'Error 404. Page could not be found.'

@app.route('/')
def default():
    return 'Please enter route in url using format localhost:5000/play/"number"/"color" where values in quotations are optional'

@app.route('/play')
def level_one():
    return render_template('index.html',amount=3,color='cornflowerblue')

@app.route('/play/<int:amount>')
def level_two(amount):
    return render_template('index.html', amount=amount,color='cornflowerblue')

@app.route('/play/<int:amount>/<string:color>')
def level_three(amount, color):
    return render_template('index.html', amount=amount,color=color)

if __name__=="__main__":       
    app.run(debug=True)    

