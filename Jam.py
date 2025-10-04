# jam.py
import time
import os

try:
    while True:
        os.system("clear")  # Bersihkan layar terminal
        print(time.strftime("⏰ %H:%M:%S", time.localtime()))
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram dihentikan.")
