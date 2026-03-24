import serial
import time
import sys

print("Приклад портів: COM3 (Windows) або /dev/ttyUSB0 (Linux)")
port_name = input("Введіть назву порту: ").strip()
baud_rate = 115200

try:
    # Відкриваємо порт
    with serial.Serial(port_name, baud_rate, timeout=1) as ser:
        print(f"Успішно підключено до {port_name} на швидкості {baud_rate} бод.")
        
        # Дані для відправки
        message = b"Test_Data" 
        ser.write(message)
        print(f"Відправлено на МК: {message.decode()}")
        
        # Чекаємо відповідь від мікроконтролера
        time.sleep(0.1)
        
        if ser.in_waiting > 0:
            response = ser.read(ser.in_waiting).decode('utf-8').strip()
            print(f"Отримано відповідь від МК: {response}")
        else:
            print("МК не відповів. Перевірте підключення або прошивку.")
            
except serial.SerialException as e:
    print(f"Помилка відкриття порту: {e}")
except Exception as ex:
    print(f"Сталася помилка: {ex}")
    
input("\nНатисніть Enter для виходу...")

