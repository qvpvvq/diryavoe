<<<<<<< HEAD
from flask import Blueprint, render_template, request, redirect, url_for, session
from database import get_db

simple_page = Blueprint('simple_page', __name__)
=======
from flask import Blueprint, request, redirect, session, jsonify
from database import get_db

simple_page = Blueprint("simple_page", __name__)

>>>>>>> 3a28698 (сделал api, обработку запроса на странице login(остальные роуты не работают))

@simple_page.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
<<<<<<< HEAD
    
    if request.method == 'POST':
        username = session.get('username')
        content = request.form.get('content')
        
        if username and content:
            db.execute("INSERT INTO posts (username, content) VALUES (?, ?)", (username, content))
            db.commit()
            return redirect(url_for('simple_page.index'))

    posts = db.execute("SELECT username, content FROM posts ORDER BY id DESC").fetchall()
    return render_template("index.html", posts=posts)


@simple_page.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        db = get_db()
        
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        user = db.execute(query).fetchone()
        
        if user:
            session.clear() # На всякий случай чистим старое
            session['username'] = user['username']
            session['role'] = user['role']
            session['user_id'] = user['id']
            return redirect(url_for('simple_page.index'))
        
        return "<h1>Ошибка входа!</h1>"
    return render_template("login.html")

@simple_page.route("/logout")
def logout():
    session.clear()  
    return redirect(url_for('simple_page.index'))

@simple_page.route("/register", methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role', 'user')

        db = get_db()
        check_user = db.execute(f"SELECT * FROM users WHERE username = '{username}'").fetchone()
        
=======

    if request.method == "POST":
        username = session.get("username")
        content = request.form.get("content")

        if username and content:
            db.execute(
                "INSERT INTO posts (username, content) VALUES (?, ?)",
                (username, content),
            )
            db.commit()
            return redirect(url_for("simple_page.index"))

    posts = db.execute(
        "SELECT username, content FROM posts ORDER BY id DESC"
    ).fetchall()
    return render_template("index.html", posts=posts)


@simple_page.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    db = get_db()

    query = (
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    )

    user = db.execute(query).fetchone()

    if user:
        session.clear()  # На всякий случай чистим старое
        session["username"] = user["username"]
        session["role"] = user["role"]
        session["user_id"] = user["id"]

        return jsonify(
            {
                "status": "ok",
                "message": "Вход выполнен",
                "user": {"username": user["username"], "role": user["role"]},
            }
        ), 200
    return jsonify({"status": "error", "error": "Неверный логин или пароль"}), 401


@simple_page.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role", "user")

        db = get_db()
        check_user = db.execute(
            f"SELECT * FROM users WHERE username = '{username}'"
        ).fetchone()

>>>>>>> 3a28698 (сделал api, обработку запроса на странице login(остальные роуты не работают))
        if check_user:
            error = "Пользователь с таким именем уже существует!"
        else:
            try:
<<<<<<< HEAD
                db.execute(f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password}', '{role}')")
                db.commit()
                return redirect(url_for('simple_page.login'))
=======
                db.execute(
                    f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password}', '{role}')"
                )
                db.commit()
                return redirect(url_for("simple_page.login"))
>>>>>>> 3a28698 (сделал api, обработку запроса на странице login(остальные роуты не работают))
            except Exception as e:
                error = f"Ошибка при регистрации: {e}"

    return render_template("register.html", error=error)

<<<<<<< HEAD
@simple_page.route("/search", methods=['GET', 'POST'])
def search():
    query = request.args.get('q') or request.form.get('q', '')
=======

@simple_page.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("q") or request.form.get("q", "")
>>>>>>> 3a28698 (сделал api, обработку запроса на странице login(остальные роуты не работают))
    users = []

    if query:
        db = get_db()
        sql = f"SELECT username FROM users WHERE username LIKE '%{query}%'"
<<<<<<< HEAD
        
        try:
            users = db.execute(sql).fetchall()
        except Exception as e:
            return f"<h1>SQL Error:</h1><pre>{e}</pre>" # подарок

    return render_template("search.html", users=users, query=query)

@simple_page.route("/admin")
def admin_page():
    # Дырявая проверка: просто смотрим роль в сессии
    if session.get('role') != 'admin':
        return "<h1>403 Доступ запрещен! Ты не админ.</h1>", 403
    
    db = get_db()

    
    users = db.execute('SELECT * FROM users').fetchall()
    posts = db.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    return render_template("admin.html", posts=posts, users=users)

@simple_page.route("/admin/delete/<int:post_id>")
def delete_post(post_id):
    if session.get('role') != 'admin':
        return "<h1>Хакер детектед!</h1>", 403
    
    db = get_db()
    db.execute(f"DELETE FROM posts WHERE id = {post_id}")
    db.commit()
    return redirect(url_for('simple_page.admin_page'))
=======

        try:
            users = db.execute(sql).fetchall()
        except Exception as e:
            return f"<h1>SQL Error:</h1><pre>{e}</pre>"  # подарок

    return render_template("search.html", users=users, query=query)


@simple_page.route("/admin")
def admin_page():
    # Дырявая проверка: просто смотрим роль в сессии
    if session.get("role") != "admin":
        return "<h1>403 Доступ запрещен! Ты не админ.</h1>", 403

    db = get_db()

    users = db.execute("SELECT * FROM users").fetchall()
    posts = db.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    return render_template("admin.html", posts=posts, users=users)


@simple_page.route("/admin/delete/<int:post_id>")
def delete_post(post_id):
    if session.get("role") != "admin":
        return "<h1>Хакер детектед!</h1>", 403

    db = get_db()
    db.execute(f"DELETE FROM posts WHERE id = {post_id}")
    db.commit()
    return redirect(url_for("simple_page.admin_page"))
>>>>>>> 3a28698 (сделал api, обработку запроса на странице login(остальные роуты не работают))
