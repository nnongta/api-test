from flask import Flask

app = Flask(__name__)

@app.route('/getcode')
def get_code():
    return "Hello, this is your code!"

@app.route('/plus/<int:num1>/<int:num2>')
def plus(num1, num2):
    return str(num1 + num2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
