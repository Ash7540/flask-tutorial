import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DATABASE = 'database.db'

# Create a table if it doesn't exist


def create_table():
    conn = sqlite3.connect(DATABASE)
    conn.execute(
        'CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    conn.close()


create_table()

# Render form to add a student


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/enternew")
def index():
    return render_template("student.html")

# Add a new student to the database


@app.route('/addrec', methods=['POST'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (nm, addr, city, pin))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close()
            return render_template("result.html", msg=msg)

# Display list of students


@app.route('/list')
def list():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)

# Render form to delete a student


@app.route("/delete")
def delete():
    return render_template("delete_record.html")

# Delete a student record


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    name = request.form["name"]
    with sqlite3.connect(DATABASE) as con:
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM students WHERE name = ?", (name,))
            msg = "Record successfully deleted"
        except:
            msg = "Can't be deleted"
        finally:
            con.close()
            return render_template("delete_record.html", msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
