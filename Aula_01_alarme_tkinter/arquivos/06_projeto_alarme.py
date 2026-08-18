import tkinter as tk
import datetime #necessario para current time
import time # necessario para atrasar a execucao do relogio, para nao encher o log
import os # necessario condicional alarm

def alarm():
    while True:
        set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
        time.sleep(1)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')  #formata hora
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            os.system('start .\\alarm-rooster.wav')
            break

root = tk.Tk()
root.geometry("400x200")
root.title("Alarme em Python")

tk.Label(root, text="Alarme", font="Helvetica 20 bold").pack(pady=15)
tk.Label(root, text="Definir Alarme").pack(pady=5)


frame = tk.Frame(root)
frame.pack()

def option(value):
    opt = tk.StringVar(root)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60)

tk.Button(root, text='Definir', font=('Helvetica 15'), command=alarm).pack(pady=20)


root.mainloop()