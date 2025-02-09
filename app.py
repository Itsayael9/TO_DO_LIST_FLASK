from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample task data (use a database in production)
tasks = []

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace this with actual user authentication logic
        if username == 'aya' and password == '123':
            session['username'] = username
            return redirect(url_for('index'))
        return "Invalid credentials, please try again."
    return render_template('login.html')

# Route for the main to-do list page
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', tasks=tasks)
    return redirect(url_for('login'))

# Route to log out
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Route to add a task
@app.route('/add', methods=['POST'])
def add_task():
    if 'username' in session:
        task_name = request.form['task_name']
        task_date = request.form['task_date']
        tasks.append({'name': task_name, 'date': task_date, 'done': False})
        return redirect(url_for('index'))
    return redirect(url_for('login'))

# Route to toggle a task as done or not done
@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 'username' in session:
        if 0 <= task_id < len(tasks):
            tasks[task_id]['done'] = not tasks[task_id]['done']
        return redirect(url_for('index'))
    return redirect(url_for('login'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'username' in session:
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
        return redirect(url_for('index'))
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)
