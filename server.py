import socket
import sys


# Create a socket object
def create_socket():
    global host
    global port
    global s

    try:
        host = ""
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow the server to reuse the port after restarting
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("Socket created successfully.")

    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        sys.exit()


# Bind the socket to the specified host and port
def bind_socket():
    global host
    global port
    global s

    while True:
        try:
            print("Binding the Port: " + str(port))

            s.bind((host, port))
            s.listen(5)

            print("Server is listening on port " + str(port))
            break

        except socket.error as msg:
            print("Socket binding error: " + str(msg))
            print("Unable to bind to port " + str(port))

            # Close the old socket
            s.close()

            # Create a new socket
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except socket.error as socket_msg:
                print("Socket recreation error: " + str(socket_msg))
                sys.exit()

            print("Retrying...")


# Establish connection with a client
def socket_accept():
    while True:
        try:
            conn, address = s.accept()

            print(
                "Connection has been established! | IP "
                + address[0]
                + " | Port "
                + str(address[1])
            )

            send_commands(conn)

            conn.close()

        except socket.error as msg:
            print("Socket accept error: " + str(msg))


# Send commands to the connected client
def send_commands(conn):
    while True:
        try:
            cmd = input()

            if cmd == "quit":
                conn.close()
                s.close()
                sys.exit()

            if len(cmd) > 0:
                conn.send(cmd.encode())

                client_response = conn.recv(1024).decode("utf-8")

                print(client_response, end="")

        except socket.error as msg:
            print("Socket communication error: " + str(msg))
            break

        except KeyboardInterrupt:
            print("\nServer shutting down...")
            conn.close()
            s.close()
            sys.exit()


# Main function
def main():
    create_socket()
    bind_socket()
    socket_accept()


# Program entry point
if __name__ == "__main__":
    main()