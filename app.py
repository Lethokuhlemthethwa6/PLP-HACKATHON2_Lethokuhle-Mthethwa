from flask import Flask, render_template, request, redirect, url_for # pyright: ignore[reportMissingImports]
from config import Config
from models import init_db, create_tables, mysql
from utils import get_ai_tip

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

@app.before_first_request
def setup():
    create_tables()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_entry():
    mood = request.form["mood"]
    reflection = request.form["reflection"]
    user_id = 1  # For now, assume single user

    # Save to DB
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO entries (user_id, mood, reflection) VALUES (%s, %s, %s)",
                   (user_id, mood, reflection))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("entries"))

@app.route("/entries")
def entries():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT mood, reflection, created_at FROM entries ORDER BY created_at DESC")
    rows = cursor.fetchall()
    cursor.close()

    return render_template("entries.html", entries=rows, ai_tip=get_ai_tip("I feel " + rows[0][0]))

if __name__ == "__main__":
    app.run(debug=True)
