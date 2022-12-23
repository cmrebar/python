from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again'

@app.route('/')
def hello():
    return render_template('index.html', phrase='hello', times=5)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

