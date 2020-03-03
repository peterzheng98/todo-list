from flask import Flask, render_template, request, redirect
from mainForms import addWorkForm
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = 'pikachu-loves-watermelon'
overall_list = []


@app.route('/')
def hello_world():
    return render_template('index.html',
                           day_string=time.strftime('%Y-%m-%d', time.localtime(time.time()))
                           )


@app.route('/addWork', methods=['GET', 'POST'])
def addWork():
    transForm = addWorkForm()
    if request.method == 'GET':
        return render_template('addWork.html', forms=transForm)
    else:
        title = request.form.get('title')
        context = request.form.get('context')
        addTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        overall_list.append((title, context, addTime))
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
