from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manager",
    database="hospital_db"
)

cursor = conn.cursor()

@app.route('/')
def dashboard():

    cursor.execute("SELECT COUNT(*) FROM Patients")
    patients = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(cost) FROM Treatments")
    revenue = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Appointments")
    appointments = cursor.fetchone()[0]

    return render_template(
        'dashboard.html',
        patients=patients,
        revenue=revenue,
        appointments=appointments
    )

if __name__ == '__main__':
    app.run(debug=True)