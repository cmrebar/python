from flask import Flask, render_template, abort, jsonify, request, redirect
import sys
app = Flask(__name__)

@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'error code': 404, 'message':'Route not found'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print('Got Post Info', file=sys.stderr)
    print(request.form, file=sys.stderr)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)