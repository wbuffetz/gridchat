# GRIDCHAT - Terminal Chat App with Secure User Management

GRIDCHAT is a simple, terminal-based chat application designed for local network use. It features real-time messaging, user authentication, and admin-controlled account management. Built using Python, it leverages file-based communication and `prompt_toolkit` for a clean and interactive CLI experience.

---

## 🚀 Features

- ✅ Terminal chat interface with timestamps
- ✅ Real-time message updates
- ✅ Secure user management with password hashing (bcrypt)
- ✅ Admin-required authentication for deleting accounts
- ✅ Password change feature with old-password verification
- ✅ Password confirmation for account creation and updates
- ✅ Simple to run and modify, built for learning and lightweight collaboration

---

## 📁 Project Structure

- /gridchat
- chat.py # Main chat client
- chatadduser.py # User management tool
- /tmp/chat/messages.txt # Chat message log (auto-created)
- /usr/local/etc/chat_users.json # JSON-based user database

## 🔐 User Management

The user management script lets you:

- Add new users
- Delete existing users (requires admin password)
- Change passwords (requires old password)

```bash
$ python3 chatadduser.py
Choose an action: [add/delete/change_password]:
```

## 🛠 Requirements

- Python3
- prompt_toolkit
- bcrypt
- lolcat and toilet (optional, for banner visuals)

```bash
pip install prompt_toolkit bcrypt
```
```bash
sudo apt install toilet lolcat  # For Debian-based systems
```

## 🔧 Running the Chat

1. Start the client
```bash
python3 chatadduser.py #add a user first
python3 gridchat.py #start the chat room after creating a user
```
2. Authenticate with your username and password
3. Start chatting!

Chat Commands
- exit – leave the chat
- clear – clear the chat display
- help – show help
  

## 👮 Admin Role

- A user named admin can authorize deletions
- When someone tries to delete a user, they must enter the admin password

Make sure to create an admin user:
```bash
python3 chatadduser.py
# Choose: add
# Username: admin
```


## 💡 Notes

- This app is meant for local testing or learning. It does not use networking or sockets.
- Consider replacing the file-based system with sockets or a database for real deployment.
- All messages are stored in a text file under /tmp/chat/messages.txt.



## 📜 License

This project is open-source. You are free to modify and share it.


## 🙌 Acknowledgements

prompt_toolkit for interactive CLI
bcrypt for secure password hashing
