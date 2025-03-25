import sqlite3

conn = sqlite3.connect('car_plate_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS car_plates 
            (NumberPlate TEXT, Date TEXT, Time TEXT)''')

with open('car_plate_data.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 2:
            license_plate = parts[0]
            datetime_str = parts[1]
            if ' ' in datetime_str:
                date_str, time_str = datetime_str.split(' ', 1)
                c.execute("INSERT INTO car_plates VALUES (?, ?, ?)", (license_plate, date_str, time_str))
            else:
                print(f"Invalid datetime format: {datetime_str}")
        else:
            print(f"Invalid line format: {line.strip()}")

conn.commit()
conn.close()