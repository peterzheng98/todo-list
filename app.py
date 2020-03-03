from flask import Flask, render_template, request, redirect
from mainForms import addWorkForm
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = 'pikachu-loves-watermelon'
overall_list = []


@app.route('/detail/<int:ident>')
def disp_detail(ident):
    sublist = overall_list[ident]
    return render_template('detail.html',
                           table_content=[('Title', sublist[0]), ('Context', sublist[1]), ('Add Time', sublist[2])],
                           overall_id=ident)


@app.route('/')
def hello_world():
    header_content = ['#', 'Title', 'Context', 'AddTime', 'Detail']
    table_content = []
    for idx, d in enumerate(overall_list):
        table_content.append(
            [('', '{}'.format(idx)), ('', d[0]), ('', d[1]), ('', d[2]), ('/detail/{}'.format(idx), 'Go>')])
    return render_template('index.html',
                           day_string=time.strftime('%Y-%m-%d', time.localtime(time.time())),
                           table_header=header_content,
                           table_content=table_content
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
