from flask import Flask, render_template
from mainForms import addWorkForm

app = Flask(__name__)
app.config["SECRET_KEY"] = 'pikachu-loves-watermelon'
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/addWork')
def addWork():
    transForm = addWorkForm()
    return render_template('addWork.html', forms=transForm)

if __name__ == '__main__':
    app.run(debug=True)
