import socket
import thread
import client_handler as ch


def connection():
    # global count
    # print(count)
    s = socket.socket()
    host = socket.gethostname()
    port = 12348
    s.bind((host, port))
    s.listen(10)
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send('Thank you for connecting')
        thread.start_new_thread(ch.print_config, (c,))
