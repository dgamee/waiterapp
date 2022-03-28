from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index_route():
    return "Welcome"

if __name__ == '__main__':
    app.run(port=5000,debug=True)