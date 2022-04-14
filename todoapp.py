from flask import Flask, render_template, redirect, url_for, request
import re

app = Flask(__name__)

todo_list = []


@app.route('/')
def display_list():
    return render_template('todo.html', todo_list=todo_list)

@app.route('/error')
def error_page():
    return render_template('error.html')

@app.route('/submit', methods=["POST"])
def submit():
    global todo_list

    task = request.form['task']
    print(task)
    email = request.form['email']
    priority = request.form['priority']
    #if (priority == "Low" or priority == "Medium" or priority == "High") and re.search(r"\w+[@]\w+[.]\w+", email):
    #    todo_list.append((task, email, priority))
    #    return redirect(url_for('display_list'))
    #else:
        #return redirect(url_for('display_list'))
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/error')
    elif not task:
        return redirect('/error')
    elif priority == 'Priority Level':
        return redirect('/error')
    else:
        todo_list.append((task, priority, email))
    print(todo_list)
    return redirect('/')

@app.route('/clear', methods=["POST"])
def clear():
    global todo_list

    todo_list = []
    return redirect('/')

@app.route('/redirect')
def reroute():
    return redirect('/')



if __name__ == '__main__':
    app.run()
