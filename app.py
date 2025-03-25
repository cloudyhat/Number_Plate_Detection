from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('car_plate_data.db')
    c = conn.cursor()

    c.execute("SELECT * FROM car_plates")
    data = c.fetchall()

    conn.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
