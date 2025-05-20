#!/usr/bin/env python3
import os
import sys
import json
import time
import threading
import bcrypt
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.application import get_app

USERS_FILE = "chat_users.json"
CHAT_FILE = "messages.txt"

def authenticate_user():
    session = PromptSession()

    username = session.prompt("Username: ")
    password = session.prompt("Password: ", is_password=True)

    try:
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
        if username in users and bcrypt.checkpw(password.encode(), users[username].encode()):
            return username
        else:
            print("Invalid credentials.")
            exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def read_chat_lines(last_pos):
    try:
        with open(CHAT_FILE, 'r') as f:
            f.seek(last_pos)
            lines = f.readlines()
            new_pos = f.tell()
            return lines, new_pos
    except FileNotFoundError:
        return [], last_pos
def chat_updater(username, stop_event):
    last_pos = 0
    while not stop_event.is_set():
        lines, last_pos = read_chat_lines(last_pos)
        for line in lines:
            # Avoid echoing own messages twice
            if not line.strip().endswith(f"{username}:"):
                print(line, end="", flush=True)
        time.sleep(0.5)
def clear_line_above():
    # Move cursor up and clear the line (ANSI escape)
    print("\033[F\033[K", end="")

def clear_screen():
    # Works on Unix and Windows
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

def print_banner():
    # This runs the shell command and prints the banner with colors forced
    os.system('echo "\e[38;5;196m$(toilet -f mono12 \'GRIDCHAT\' -w 100 | lolcat)\e[0m"')
def helpfunc():
    print(f"Type /exit to leave.\n")
    print(f"Type /clear to clear screen.\n")

def main():
    print_banner()

    username = authenticate_user()

    os.makedirs(os.path.dirname(CHAT_FILE), exist_ok=True)
    if not os.path.exists(CHAT_FILE):
        open(CHAT_FILE, 'w').close()

    stop_event = threading.Event()
    updater_thread = threading.Thread(target=chat_updater, args=(username, stop_event))
    updater_thread.daemon = True
    updater_thread.start()

    session = PromptSession()
    clear_screen()
    print(f"Welcome, {username}! Type /exit to leave.\n")
    print(f"Type /help for help.\n")
    with patch_stdout():
        while True:
            try:
                msg = session.prompt("> ").strip()
                if msg != "":
                    os.write(sys.stdout.fileno(), b"\033[F\033[K")

                if msg.lower() == "/exit":
                    break
                if msg.lower() == "/clear":
                    clear_screen()
                    print(f"Chat cleared. Type /exit to leave.\n")
                    continue
                if msg.lower() == "/help":
                    helpfunc()
                    continue
                if msg == "":
                    continue
                timestamp = time.strftime("[%H:%M:%S]")
                with open(CHAT_FILE, 'a') as f:
                    f.write(f"{timestamp} {username}: {msg}\n")
            except (KeyboardInterrupt, EOFError):
                break

    stop_event.set()
    updater_thread.join()
    print("Goodbye.")

if __name__ == "__main__":
    main()
