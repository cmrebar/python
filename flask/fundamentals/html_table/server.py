from flask import Flask, render_template, abort, jsonify
app = Flask(__name__)

@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

@app.route('/users')
def table():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('index.html',users=users)

if __name__=="__main__":       
    app.run(debug=True)