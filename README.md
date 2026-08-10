# TCP/IP Socket Programming in Python (Reverse Shell)

A simple, lightweight implementation of a remote command execution system (Reverse Shell) built using Python's standard `socket` and `subprocess` libraries. 

This repository demonstrates the fundamentals of TCP/IP networking, multi-function script architecture, and remote system interaction.

---

## 🛠 Features

- **Port Reusability:** The server includes `SO_REUSEADDR` to avoid "Address already in use" errors during quick restarts.
- **Fail-Safe Binding:** The server runs a continuous loop to safely retry binding if the network interface is temporarily locked.
- **Directory Navigation:** The client dynamically processes `cd` commands to change working directories seamlessly on the target system.
- **Full Output Retrieval:** Captures both standard output (`stdout`) and standard error (`stderr`) streams from executed commands.

---

## 🏗 System Architecture

The project consists of two core files:

1. **`server.py` (The Controller):** 
   - Listens on port `9999` for incoming connections.
   - Accepts an incoming client connection.
   - Operates an interactive prompt to send terminal commands down to the client.

2. **`client.py` (The Target):**
   - Connects out to the server's specific IP and port.
   - Awaits incoming command strings.
   - Executes commands locally via a hidden background process shell and routes the console output back to the server.

---

## 🚀 How to Run the Project

### Prerequisites
Make sure you have Python 3.x installed on both machines.

### Step 1: Configure the Client IP
Before running the files, open `client.py` and update the `host` variable to match the exact local or remote IP address of the machine running your server.

```python
# In client.py
host = 'YOUR_SERVER_IP_HERE'  # e.g., '10.150.42.166'
```

### Step 2: Start the Server
Always launch the listener/server first so it is ready to receive the connection.

```bash
python server.py
```

### Step 3: Start the Client
Run the client script on the target computer.

```bash
python client.py
```

Once the connection is established, the server terminal will print a success log. You can then type standard terminal commands (e.g., `dir`, `ls`, `whoami`, `cd ..`) directly into the server to execute them remotely. Type `quit` to safely close the connection.

---

## ⚠️ Disclaimer
This project is intended strictly for **educational purposes** and **authorized security testing** environments. Do not execute or deploy this software on systems without explicit permission from the owner.
