import os
import webbrowser
import subprocess
from pomodoro_timer import PomodoroTimer

# Define paths for VS Code and Notepad
vscode_path = os.path.join(os.environ['LocalAppData'], 'Programs\\Microsoft VS Code\\Code.exe')
notepad_path = 'C:\\windows\\system32\\notepad.exe'

def open_webpage(url):
    webbrowser.open(url)

def open_vscode():
    subprocess.Popen(vscode_path)

def open_notepad():
    subprocess.Popen(notepad_path)

# Example usage
youtube_url = "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl" 
#open_webpage(youtube_url)
#open_vscode()
#open_notepad()

work_minutes = int(input("how many minutes do you want to work for?   "))
break_minutes = int(input("how many minutes do you want to take a break for?   "))
timer = PomodoroTimer(work_minutes,break_minutes)
timer.root.mainloop()
