from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<p>Wassuppp, Flask!</p>"

@app.route('/bye')
def goodbye_flask():
    return "<p>Goodbye, Flask!</p>"

@app.route('/username/<name>/<int:number>')
def greet_user(name, number):
    return f"{name} is learning Flask!! {number} times"

# if __name__ == '__main__':
#     app.run(debug=True)
