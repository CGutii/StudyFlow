import time
import threading
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import Theme

class PomodoroTimer:
    def __init__(self, work_minutes, break_minutes):
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes
        self.is_work_time = True

        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")
        self.root.geometry("200x300")
        self.root.resizable(False, False)

        self.theme = Theme.Theme(self.root)

        self.frame = tk.Frame(self.root)
        self.theme.add(self.frame, "bg", "white", "#000000")
        self.frame.pack(expand=True)

        self.time_left_label = tk.Label(self.frame, text="", font=("Arial", 25))
        self.theme.add(self.time_left_label, "bg", "white", "#000000")
        self.theme.add(self.time_left_label, "fg", "black", "#FFD700")
        self.time_left_label.pack(pady=20)

        self.clock_label = tk.Label(self.frame, font=("Arial", 10))
        self.theme.add(self.clock_label, "bg", "white", "#000000")
        self.theme.add(self.clock_label, "fg", "black", "#FFD700")
        self.clock_label.pack(pady=10)

        button_frame = tk.Frame(self.frame)
        self.theme.add(button_frame, "bg", "white", "#000000")
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, font=("Arial", 8), padx=8, pady=4)
        self.theme.add(self.start_button, "bg", "white", "#000000")
        self.theme.add(self.start_button, "fg", "black", "#FFD700")
        self.start_button.pack(side='left', padx=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer, font=("Arial", 8), padx=8, pady=4)
        self.theme.add(self.pause_button, "bg", "white", "#000000")
        self.theme.add(self.pause_button, "fg", "black", "#FFD700")

        self.resume_button = tk.Button(button_frame, text="Resume", command=self.resume_timer, font=("Arial", 8), padx=8, pady=4)
        self.theme.add(self.resume_button, "bg", "white", "#000000")
        self.theme.add(self.resume_button, "fg", "black", "#FFD700")

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer, font=("Arial", 8), padx=8, pady=4)
        self.theme.add(self.reset_button, "bg", "white", "#000000")
        self.theme.add(self.reset_button, "fg", "black", "#FFD700")

        self.pause_event = threading.Event()
        self.stop_event = threading.Event()
        self.pause_event.set()
        self.stop_event.clear()
        self.countdown_thread = None

        threading.Thread(target=self.update_clock).start()

    def start_timer(self):
        self.start_button.pack_forget()
        self.pause_button.pack(side='left', padx=5)
        self.reset_button.pack(side='left', padx=5)
        if self.countdown_thread is None or not self.countdown_thread.is_alive():
            self.stop_event.clear()
            self.countdown_thread = threading.Thread(target=self.countdown, args=(self.work_minutes if self.is_work_time else self.break_minutes,))
            self.countdown_thread.start()

    def pause_timer(self):
        self.pause_button.pack_forget()
        self.resume_button.pack(side='left', padx=5)
        self.pause_event.clear()

    def resume_timer(self):
        self.resume_button.pack_forget()
        self.pause_button.pack(side='left', padx=5)
        self.pause_event.set()

    def reset_timer(self):
        self.stop_event.set()
        if self.countdown_thread and self.countdown_thread.is_alive():
            self.countdown_thread.join()
        self.time_left = self.work_minutes * 60 if self.is_work_time else self.break_minutes * 60
        mins, secs = divmod(self.time_left, 60)
        self.time_left_label.config(text="{:02d}:{:02d}".format(mins, secs))
        self.start_button.pack(side='left', padx=5)
        self.pause_button.pack_forget()
        self.resume_button.pack_forget()

    def countdown(self, minutes):
        self.time_left = minutes * 60
        while self.time_left > 0 and not self.stop_event.is_set():
            self.pause_event.wait()
            mins, secs = divmod(self.time_left, 60)
            self.time_left_label.config(text="{:02d}:{:02d}".format(mins, secs))
            time.sleep(1)
            self.time_left -= 1
        if not self.stop_event.is_set():
            self.root.after(0, self.show_message)

    def show_message(self):
        if self.is_work_time:
            messagebox.showinfo("Break Time", "Take a break, you deserve it! 😌")
        else:
            messagebox.showinfo("Work Time", "Time to get back to work! You've got this! 💪")
        self.is_work_time = not self.is_work_time
        self.start_timer()

    def update_clock(self):
        while True:
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S %p")
            self.clock_label.config(text=current_time)
            time.sleep(1)

if __name__ == "__main__":
    work_minutes = 25
    break_minutes = 5
    pomodoro = PomodoroTimer(work_minutes, break_minutes)
    pomodoro.root.mainloop()
