from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.user import User
from app.extensions import db
from flask_login import login_user

auth_register_bp = Blueprint("auth_register", __name__)


@auth_register_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Pobranie danych z formularza
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        phone_number = request.form.get("phone_number")
        date_of_birth = request.form.get("date_of_birth")

        # Walidacja podstawowych pól
        if not all([first_name, last_name, email, password]):
            flash("Proszę wypełnić wszystkie wymagane pola", "error")
            return redirect(url_for("register.register"))

        # Sprawdzenie czy email już istnieje
        if User.query.filter_by(email=email).first():
            flash("Email już istnieje w systemie", "error")
            return redirect(url_for("register.register"))

        # Sprawdzenie czy numer telefonu już istnieje (jeśli podany)
        if (
            phone_number
            and User.query.filter_by(phone_number=phone_number).first()
        ):
            flash("Numer telefonu już istnieje w systemie", "error")
            return redirect(url_for("register.register"))

        # Tworzenie nowego użytkownika
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            prefix=request.form.get("prefix", ""),
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            address=request.form.get("address"),
            city=request.form.get("city"),
            state=request.form.get("state"),
            zip_code=request.form.get("zip_code"),
            country=request.form.get("country"),
            is_active=True,
            is_admin=False,
        )

        # Ustawienie hasła
        new_user.set_password(password)

        # Zapis do bazy danych
        try:
            db.session.add(new_user)
            db.session.commit()
            flash(
                "Rejestracja zakończona sukcesem! Możesz się zalogować.",
                "success",
            )

            # Automatyczne logowanie po rejestracji
            login_user(new_user)
            return redirect(url_for("dashboard.dashboard"))

        except Exception as e:
            db.session.rollback()
            flash("Wystąpił błąd podczas rejestracji: " + str(e), "error")

    # Dla metody GET wyświetl formularz
    return render_template("auth/register.html")
