from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1><font color=red>Germinare Tech, EU AMO DEVOPS.. MAS NÃO TANTO QUANTO SUA MÃE ..</font></h1></center> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
