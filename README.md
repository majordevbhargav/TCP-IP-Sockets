# TCP/IP Socket Programming

A small Python networking project demonstrating TCP client/server communication, socket programming, and remote command execution in an explicitly authorized lab environment.

## Overview

The project contains a controller/server and a client that communicate over TCP. It is intended to demonstrate low-level networking concepts such as sockets, connection handling, command transport, and process output.

## Architecture

```text
Controller / Server
       │
       │ TCP connection
       ▼
Client / Target
       │
       ▼
Local command execution
       │
       └── stdout / stderr
             ↓
          Server
```

## Components

- `server.py` listens for connections and provides the interactive controller side.
- `client.py` connects to the configured server and handles the received command workflow.

## Technology

- Python 3.x
- `socket`
- `subprocess`

## Lab Setup

Use this project only on systems you own or are explicitly authorized to test.

Configure the server address in the client according to your isolated lab environment, then start the listener before the client.

```bash
python server.py
```

In the authorized test environment:

```bash
python client.py
```

## Networking Concepts Demonstrated

- TCP sockets
- Client/server architecture
- Connection lifecycle
- Port binding
- Data transmission
- Standard output and error handling
- Basic command transport

## Security Note

This project can execute commands on the connected client and therefore has security implications. Do not deploy it against third-party systems, production endpoints, or networks without explicit authorization.

## Future Direction

- Explicit authentication
- Encrypted transport
- Structured message protocol
- Safer command allowlists
- Connection logging
- Educational packet-flow visualization

## Author

**Dev Bhargav**

- GitHub: https://github.com/majordevbhargav
- LinkedIn: https://www.linkedin.com/in/devbhargav100
