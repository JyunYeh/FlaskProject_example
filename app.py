from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # jinja 2 example:
    list = [1,2,3,4,5]
    return render_template('index.html', list = list)


@app.route('/head')
def head():
    return render_template('header.html')

if __name__ == '__main__':
    app.run(debug=True)

