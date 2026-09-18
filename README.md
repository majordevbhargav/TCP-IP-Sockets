# TCP/IP Socket Programming

A small Python networking project for learning **TCP sockets, client/server communication, connection handling, and data transport**.

## Architecture

```text
Server
  |
  | TCP connection
  v
Client
  |
  v
Data / command workflow
  |
  v
Response
```

## Concepts Practiced

- TCP sockets
- Client/server architecture
- Port binding
- Connection lifecycle
- Sending and receiving data
- Error handling
- Process communication

## Technology

- Python 3
- `socket`
- `subprocess`

## Learning Purpose

This is an intentionally small project. The goal is to understand what happens underneath higher-level networking frameworks before moving into larger network automation and security projects.

It is part of my progression from **networking fundamentals → Python → automation → network security**.

## Security

The project can perform command execution in the connected client workflow. Use it only in systems and networks you own or are explicitly authorized to test.

Do not deploy it against third-party or production systems.

## Future Direction

- Authentication
- Encrypted transport
- Structured protocol
- Command allowlists
- Connection logging
- Packet-flow visualization

## Author

**Dev Bhargav**

[GitHub](https://github.com/majordevbhargav) · [LinkedIn](https://www.linkedin.com/in/devbhargav100)
