from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user
from app.models.user import User

auth_login_bp = Blueprint("auth_login", __name__)


@auth_login_bp.route("/login", methods=["GET", "POST"])
def login():
    # Jeśli użytkownik jest już zalogowany, przekieruj go do dashboardu
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Walidacja pól formularza
        if not email or not password:
            flash("Proszę wypełnić wszystkie pola", "error")
            return redirect(url_for("login.login"))

        # Znajdź użytkownika w bazie danych
        user = User.query.filter_by(email=email).first()

        # Sprawdź czy użytkownik istnieje i hasło jest poprawne
        if user and user.check_password(user.password_hash, password):
            login_user(user)
            flash("Zalogowano pomyślnie!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("dashboard.dashboard"))
        else:
            flash("Nieprawidłowy email lub hasło", "error")

    return render_template("auth/login.html")
