from flask import Flask, render_template, abort, jsonify
app = Flask(__name__)

@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

@app.route('/')
def default():
    return render_template('index.html',x=8,y=8,color1='black',color2='red')

@app.route('/<int:x>')
def rows(x):
    return render_template('index.html',x=x,y=8,color1='black',color2='red')

@app.route('/<int:x>/<int:y>')
def rowsAndColumns(x,y):
    return render_template('index.html',x=x,y=y,color1='black',color2='red')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def everything(x,y,color1,color2):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

if __name__=="__main__":       
    app.run(debug=True) 