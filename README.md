# Study Environment Setup Script

**study.py** is a Python script designed to help computer science students quickly set up a study or programming environment. It opens a lo-fi YouTube stream, launches VS Code, a Pomodoro timer, and a notepad, providing a focused and productive atmosphere for studying or coding sessions. This document provides an overview of the script's functionality and usage instructions.

## Features

1. **YouTube Stream** : The script opens a lo-fi YouTube stream to create a calming and immersive study environment.
2. **VS Code Integration** : VS Code, a popular code editor, is automatically launched for coding tasks.
3. **Pomodoro Timer** : The Pomodoro technique is implemented with a configurable timer that alternates between work and break periods.
4. **Notepad** : A notepad application is opened, allowing users to take quick notes during their study session.

## Prerequisites

- Python 3.x installed on your system.
- An internet connection to access the lo-fi YouTube stream.
- [VS Code](https://code.visualstudio.com/) installed on your system.

## Installation

1. Download the project files from the repository and store them in a convenient location on your system.
2. Install the required Python dependencies
3. Ensure that the paths for VS Code and the notepad application are correctly configured in the `study.py` file. Modify the `vscode_path` and `notepad_path` variables if necessary.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the `study.py` file is located.
2. Run the following command to start the study environment setup:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python study.py
</code></div></div></pre>

3. The script will open the lo-fi YouTube stream, launch VS Code, the Pomodoro timer, and the notepad. You can adjust the work and break periods at run time as the user will be prompted with the questions.
4. Utilize the Pomodoro timer to manage your work and break sessions. Click the "Start," "Pause," "Resume," and "Reset" buttons to control the timer.
5. Use the VS Code editor for coding or editing tasks. Take notes in the opened notepad as needed.
6. To stop the study environment, close the VS Code editor and the notepad window. Press `Ctrl + C` in the terminal or command prompt to terminate the script.

## Notes

- Make sure you have an active internet connection to stream the lo-fi YouTube video and access additional resources.
- As far as test have gone this script **ONLY WORK FOR WINDOWS OS** but the python code can be easily adapted.
- Ensure that your system has a media player capable of streaming YouTube audio. If the audio does not play automatically, you may need to copy the lo-fi YouTube stream URL and play it in your preferred media player manually.
- Customize the script further to suit your needs. You can modify the YouTube stream URL, add more features, or change the appearance by editing the provided files.
- For any issues or concerns, please refer to the project repository for support and updates.

This project aims to create an optimal study environment by combining various tools and resources into a single script. It is designed to enhance focus and productivity during study or coding sessions. We hope this script helps you achieve your study goals effectively. Happy studying!
