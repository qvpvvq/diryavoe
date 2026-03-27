from flask import Blueprint, render_template, request, redirect, url_for
from database import get_db

simple_page = Blueprint('simple_page', __name__)

@simple_page.route("/")
def index():
    return render_template("index.html")

@simple_page.route("/users")
def get_users():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('users.html', users=users)

@simple_page.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        db = get_db()
        
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        user = db.execute(query).fetchone()
        
        if user:
            return f"<h1>Успех! Вы вошли как {user['username']} (Роль: {user['role']})</h1>"
        else:
            return "<h1>Ошибка! Неверный логин или пароль.</h1>"
    return render_template("login.html")

@simple_page.route("/register", methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = 'user'  # По умолчанию все новые — обычные юзеры

        db = get_db()
        
        # Проверяем, нет ли уже такого юзера
        check_user = db.execute(f"SELECT * FROM users WHERE username = '{username}'").fetchone()
        
        if check_user:
            error = "Пользователь с таким именем уже существует!"
        else:
            try:
                db.execute(f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password}', '{role}')")
                db.commit()
                return redirect(url_for('simple_page.login'))
            except Exception as e:
                error = f"Ошибка при регистрации: {e}"

    return render_template("register.html", error=error)