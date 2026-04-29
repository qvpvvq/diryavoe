from flask import Blueprint, request, session, jsonify
from database import get_db

simple_page = Blueprint("simple_page", __name__)


@simple_page.route("/me", methods=["GET"])
def me():
    if session.get("username"):
        return jsonify(
            {"username": session.get("username"), "role": session.get("role")}
        ), 200
    return jsonify({"status": "error", "error": "Не авторизован"}), 401


@simple_page.route("/posts", methods=["GET", "POST"])
def index():
    db = get_db()

    if request.method == "POST":
        username = session.get("username")
        if not username:
            return jsonify({"status": "error", "error": "not authorized"}), 401
        data = request.get_json()
        content = data.get("content")
        if not content:
            return jsonify(
                {"status": "error", "error": "content of post is empty"}
            ), 400

        if username and content:
            db.execute(
                "INSERT INTO posts (username, content) VALUES (?, ?)",
                (username, content),
            )
            db.commit()
            return jsonify({"status": "ok", "message": "post created"})
    if request.method == "GET":
        posts = db.execute(
            "SELECT username, content FROM posts ORDER BY id DESC"
        ).fetchall()
        return jsonify(
            {
                "status": "ok",
                "message": "post list sent",
                "posts": [dict(post) for post in posts],
            }
        ), 200


@simple_page.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Некорректный запрос"}), 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"status": "error", "message": "No password or login"}), 400

    db = get_db()
    user = db.execute(
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    ).fetchone()

    if user:
        session.clear()
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


@simple_page.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Incorrect JSON"}), 400
    username = data.get("username")
    password = data.get("password")
    if not password or not username:
        return jsonify({"status": "error", "message": "No password or login"}), 400
    role = data.get("role", "user")

    db = get_db()
    check_user = db.execute(
        f"SELECT * FROM users WHERE username = '{username}'"
    ).fetchone()

    if check_user:
        return jsonify(
            {"status": "error", "error": "Пользователь с таким именем уже существует!"}
        ), 409
    try:
        db.execute(
            f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password}', '{role}')"
        )
        db.commit()
        return jsonify({"status": "ok", "message": "account created"}), 201

    except Exception as e:
        return jsonify({"status": "error", "error": "Непредвиденная ошибка"}), 500


@simple_page.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    users = []

    if query:
        db = get_db()

        try:
            users = db.execute(
                f"SELECT id, username FROM users WHERE username LIKE '%{query}%'"
            ).fetchall()
        except Exception:
            return jsonify({"status": "error", "error": "internal server error"}), 500

    return jsonify({"users": [dict(user) for user in users]}), 200


@simple_page.route("/admin", methods=["GET"])
def admin_page():
    if session.get("role") != "admin":
        return jsonify({"status": "error", "error": "Недостаточно прав"}), 403
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    posts = db.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    return jsonify(
        {
            "status": "ok",
            "message": "post and user list sent",
            "posts": [dict(post) for post in posts],
            "users": [dict(user) for user in users],
        }
    ), 200


@simple_page.route("/admin/posts", methods=["DELETE"])
def delete_posts():
    db = get_db()
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Incorrect JSON"}), 400
    postId = data.get("id")
    db.execute(f"DELETE FROM posts WHERE id = {postId}")
    db.commit()
    return jsonify({"status": "ok", "message": "post deleted"}), 200


@simple_page.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"status": "ok", "message": "Сессия успешно очищена"}), 200
