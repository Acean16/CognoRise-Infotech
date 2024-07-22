import threading
import time
import tkinter as tk



def start():
    global stop_loop
    stop_loop = False 

    hours, minutes, seconds = 0, 0, 0
    string_split = time_entry.get().split(":")
    if len(string_split) == 3:
        hours = int(string_split[0])
        minutes = int(string_split[1])
        seconds = int(string_split[2])
    elif len(string_split) == 2:
        minutes = int(string_split[0])
        seconds = int(string_split[1])
    elif len(string_split) == 1:
        seconds = int(string_split[0])
    else:
        print("Invalid time format")
        return
        
    full_seconds = (hours * 3600) +(minutes * 60) + seconds

    while full_seconds > 0 and not stop_loop:
        full_seconds -= 1

        minutes, seconds = divmod(full_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        time_label.config(text=f"Time:{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.update()
        time.sleep(1)

def start_thread():
    t = threading.Thread(target=start)
    t.start()

def stop():
    global stop_loop
    stop_loop = True
    time_label.config(text="Time: 00:00:00")

root = tk.Tk()
root.geometry("415x200")
root.title("Countdown Timer")

time_entry = tk.Entry(root, font=('Gothic', 30))
time_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

start_button = tk.Button(root, font=('Gothic', 30), text="Start", command = start_thread)
start_button.grid(row=1, column=0, padx=5, pady=5)

stop_button = tk.Button(root, font=('Gothic', 30), text="Stop", command = stop)
stop_button.grid(row=1, column=1, padx=5, pady=5)

time_label = tk.Label(root, font=('Gothic', 30), text="Time: 00:00:00")
time_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)



root.mainloop()

