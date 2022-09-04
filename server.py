from socket import *
# define socket port number at the port 9000.
serverPort = 9000
# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
# assign the port number to the socket.
serverSocket.bind(("", serverPort))
# the server listen for TCP connection request from one client at a time.
serverSocket.listen(1)
# print message to the user to show that the connection is established.
print("The Server is ready to receive...")

# Server should be up and running and listening to the incoming connections
while True:
    # create new socket in the server, so that the client and server can send bytes to each other.
    connectionSocket, clinet_socket = serverSocket.accept()
    # receive the request message from the client
    request_msg = connectionSocket.recv(1024).decode()
    # print the address of the user
    print(clinet_socket)
    print(request_msg)

    # extract the ip address and the port number from the client socket.
    ip = clinet_socket[0]
    port = clinet_socket[1]

    # header contains header lines and request line "the first line of the request message"
    headers = request_msg.split('\n')
    print(headers)
    # extract the url field from the request line from the request message
    # The path is the second part of request line, identified by [1]
    url_field = headers[0].split()[1]
    print(url_field)

    match url_field:
        case '/' | '/en':  # when requesting / or /en
            # Send the HTTP version to the connection socket
            # Format: "HTTP/1.1 *code-for-successful-request*\r\n\r\n"
            ##------------------------------------------------------------------------
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            # specifying the type.
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            ##-------------------------------------------utf-8
            # UTF-8--> is an encoding system for Unicode
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            # open the webpage main_en.html
            f1 = open("main_en.html", "rb")
            connectionSocket.send(f1.read())
            f1.close()

        case '/ar':  # when requesting /ar
            # Send the HTTP version to the connection socket
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            # specifying the type.
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            f1 = open("main_ar.html", "rb")
            connectionSocket.send(f1.read())
            f1.close()

        case '/other.html':  # # when requesting /other.html
            url_field = 'other.html'
            fin = open(url_field)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))

        case '/file.css':  # when requesting /file.css
            url_field = 'style.css'
            fin = open(url_field)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/css\r\n", "UTF-8"))
            print("Content-Type: text/css\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))

        case '/Network1.jpg':  # when requesting /Network1.png
            fin = open("images/download.jpg", "rb")
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: image/jpg\r\n\r\n", "UTF-8"))
            print("Content-Type: image/jpg\r\n\r\n")
            connectionSocket.send(fin.read())
            print(str(fin.read()))

        case '/Network1.png':  # when requesting /Network1.jpg
            fin = open("images/Networks.png", "rb")
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: image/jpg\r\n\r\n", "UTF-8"))
            print("Content-Type: image/png\r\n\r\n")
            connectionSocket.send(fin.read())
            print(str(fin.read()))

        case '/go':
            connectionSocket.send(bytes("HTTP/1.1 307 Temporary Redirect  \r\n", "UTF-8"))
            connectionSocket.send(bytes("Content-Type:\r\n", "UTF-8"))
            connectionSocket.send(bytes("location: http://google.com/ \r\n", "UTF-8"))
            print("Content-Type: \r\n\r\n")

        case '/cn':

            connectionSocket.send(bytes("HTTP/1.1 307 Temporary Redirect  \r\n", "UTF-8"))
            connectionSocket.send(bytes("Content-Type:\r\n", "UTF-8"))
            connectionSocket.send(bytes("location: https://edition.cnn.com/ \r\n", "UTF-8"))
            print("Content-Type: \r\n\r\n")

        case '/bzu':

            connectionSocket.send(bytes("HTTP/1.1 307 Temporary Redirect  \r\n", "UTF-8"))
            connectionSocket.send(bytes("Content-Type:\r\n", "UTF-8"))
            connectionSocket.send(bytes("location: https://www.birzeit.edu/ar \r\n", "UTF-8"))
            print("Content-Type: \r\n\r\n")

        case other_case:  # when requesting Wrong file
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            f1 = open("Error.html", "rb")
            connectionSocket.send(f1.read())
            f1.close()
