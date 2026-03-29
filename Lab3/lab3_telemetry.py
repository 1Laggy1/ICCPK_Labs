import requests
import json
import os

with open("gps_log.txt", "w", encoding="utf-8") as f:
    for i in range(1, 26):
        f.write(f"2026-02-19 07:{i:02d}, Lat: 50.45{i:02d}, Lon: 30.52{i:02d}, Speed: {40+i} km/h, Course: 120°\n")

print("Файл gps_log.txt створено.")

data = []
with open("gps_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(", ")
        if len(parts) >= 5:
            entry = {
                "time": parts[0],
                "lat": parts[1].replace("Lat: ", ""),
                "lon": parts[2].replace("Lon: ", ""),
                "speed": parts[3].replace("Speed: ", "").replace(" km/h", ""),
                "course": parts[4].replace("Course: ", "").replace("°", "")
            }
            data.append(entry)

chunk_size = 10
url = "https://httpbin.org/post"

for i in range(0, len(data), chunk_size):
    chunk = data[i:i + chunk_size]
    
    print(f"\n---> Відправка пакету з {len(chunk)} записів...")
    
    response = requests.post(url, json=chunk)
    
    if response.status_code == 200:
        print("Успішно! Сервер отримав наступні дані (поле json):")
        server_received_data = response.json().get("json")
        print(json.dumps(server_received_data, indent=2, ensure_ascii=False))
    else:
        print(f"Помилка відправки: HTTP {response.status_code}")
