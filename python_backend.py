import serial
import mysql.connector
import time

# Setup Serial Port
try:
    ser = serial.Serial('COM12', 115200, timeout=5)  # Make sure COM12 is correct
    time.sleep(2)  # Give time to ESP32 to reset and boot
    print("Serial connected.")
except Exception as e:
    print("Serial connection failed:", e)
    exit()

# Setup MySQL connection
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="esp_data",
        port=3306
    )
    cursor = conn.cursor()
    print("MySQL connected.")
except Exception as e:
    print("Database connection failed:", e)
    ser.close()
    exit()

# Start Reading Loop
try:
    while True:
        try:
            line = ser.readline().decode().strip()
            if ',' not in line:
                continue  # Skip any junk/boot messages

            parts = line.split(',')
            if len(parts) != 3:
                continue  # Not valid data

            temperature = float(parts[0])
            humidity = float(parts[1])
            lumen = int(parts[2])

            cursor.execute(
                "INSERT INTO sensor_data (temperature, humidity, Lumen) VALUES (%s, %s, %s)",
                (temperature, humidity, lumen)
            )
            conn.commit()
            print(f"Inserted: Temp={temperature}°C, Humidity={humidity}%", f"Lumen={lumen}")

        except ValueError as ve:
            print("Data parsing error:", ve)
        except Exception as e:
            print("Insert error:", e)

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    ser.close()
    conn.close()
    print("Connections closed.")
